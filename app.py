import csv
import glob
import sys
import lib
import os
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
        outfile = "{file}.{processed}".format(file=infile, processed=config.get("input").get("processed"))
        infile = csv.reader(open(outfile, "rb"))

        header = infile.next()
        header = [x.replace("-", "_") for x in header]

        for row in infile:
            data = {}
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
                data[header[i]] = item

            user_id = data.pop("user_id")
            user = lib.User(id=user_id, **data)
            session.merge(user)
        session.commit()


if __name__ == '__main__':
    # this allows us to specify a list of files
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        files = glob.glob("{path}/*.{extension}".format(**config.get("input")))
    convert_to_csv(files)
    reformat_data(files)
