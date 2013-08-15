#!/usr/bin/env python

import csv
import glob
import sys
import lib
import os
import unidecode
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


def reformat_data(files):
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
                elif item.isdigit():
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
            if "name" in user:
                names = user["name"].split()
                if len(names) >= 2:
                    user["name_first"] = names[0]
                    user["name_last"] = names[-1]
            user = lib.User(id=user_id, **user)
            for action in actions:
                user.actions.append(lib.UserAction(**action))
            session.merge(user)

            if (k + 1) % 1000 == 0:
                print " *", k + 1, datetime.now()
                session.merge(user)
                break
        session.commit()


if __name__ == '__main__':
    # this allows us to specify a list of files
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        files = glob.glob("{path}/*.{extension}".format(**config.get("input")))
    convert_to_csv(files)
    reformat_data(files)
