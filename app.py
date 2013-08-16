#!/usr/bin/env python

import csv
import glob
import sys
import lib
import os
import unidecode
import json
from datetime import datetime


config = lib.get_config()


def convert_to_csv(files):
    for infile in files:
        outfile = "{file}.{processed}".format(file=infile, processed=config.get("input").get("processed"))
        if os.path.exists(outfile):
            continue
        print " *", infile
        infile = open(infile, "rb")
        outfile = csv.writer(open(outfile, "wb"))

        header = None
        for row in infile:
            row = row.replace("\n", "")  # remove newlines
            if not header:
                if row.count('\\t') > 10:  # this is likely the header
                    header = row.split('\\t')
                    outfile.writerow(header)
            else:
                if row.count("\t") > 10:
                    data = row.split("\t")
                    data.pop(8)  # this item is weird (email sig cnt)
                    if data[1] == "":  # if url is missing
                        continue
                    outfile.writerow(data)


def reformat_data_into_db(files):
    session = lib.fetch_session()

    for infile in files:
        print infile
        outfile = "{file}.{processed}".format(file=infile, processed=config.get("input").get("processed"))
        infile = csv.reader(open(outfile, "rb"))

        header = infile.next()
        header = [x.replace("-", "_") for x in header]
        action_point = header.index("share_follow_me_video_count")

        for k, row in enumerate(infile):
            user = {}
            actions = []
            for i, item in enumerate(row):
                # convert to datevalues
                if item is "" or item is None:
                    continue
                if item[-5:] == "+0000" and len(item) < 30:
                    item = datetime.strptime(item, '%Y-%m-%d %H:%M:%S +0000')
                elif item[-3:] == "UTC" and len(item) < 30:
                    item = datetime.strptime(item, '%Y-%m-%d %H:%M:%S UTC')
                elif item.isdigit() and len(item) < 10:
                    item = int(item)
                else:
                    item = unidecode.unidecode(item)

                if i < action_point:
                    user[header[i]] = item
                else:
                    if "_count" in header[i]:
                        actions.append({
                            "count": item,
                            "action": header[i].replace("_count", "")
                        })
                    elif "_first_used_at" in header[i]:
                        actions[-1].update({"date_first": item})
                    elif "_last_used_at" in header[i]:
                        actions[-1].update({"date_last": item})

            user_id = user.pop("user_id")

            # adding location
            loc = None
            if "location" in user:
                location_id = user.pop("location")
                loc = lib.Location(id=location_id)
                session.merge(loc)

            if "name" in user and type(user["name"]).__name__ in ("str", "unicode"):
                names = user["name"].split()
                if len(names) >= 2:
                    user["name_first"] = names[0]
                    user["name_last"] = names[-1]

            user = lib.User(id=user_id, **user)
            for action in actions:
                user.actions.append(lib.UserAction(**action))
            if loc:
                user.location = loc

            session.merge(user)

            if (k + 1) % 5000 == 0:
                print " *", k + 1, datetime.now()
                session.commit()
        session.commit()


def add_creds(files):
    # tsv file
    # user_id, first_name, last_name, industry, degree
    session = lib.fetch_session()
    for infile in files:
        print infile
        for k, row in enumerate(open(infile, "rb")):
            row = row.replace("\n", "").split("\t")
            if k == 0:
                header = row
                continue
            if len(row) == 5:
                if row[header.index("industry")] or row[header.index("degree")]:
                    cred = lib.UserCred(**{
                        "user_id": row[header.index("user_id")],
                        "industry": unidecode.unidecode(row[header.index("industry")]),
                        "degree": unidecode.unidecode(row[header.index("degree")])})
                    session.merge(cred)

            if (k + 1) % 5000 == 0:
                print " *", k + 1, datetime.now()
                session.commit()
        session.commit()


if __name__ == '__main__':
    # files = glob.glob("{path}/*.{extension}".format(**config.get("input")))
    # convert_to_csv(files)
    # reformat_data_into_db(files)

    files = glob.glob("{path}_cred/*.{extension}".format(**config.get("input")))
    add_creds(files)
