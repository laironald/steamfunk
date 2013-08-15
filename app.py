import csv
import glob
import sys
import lib
import os
from datetime import datetime


config = lib.get_config()


def reformat_data(header, row):
    data = {}
    print header
    print row.split("\t")

    for i, item in enumerate(row.split("\t")):
        if item[-5:] == "+0000":
            data[header[i]] = datetime.strptime(item, '%Y-%m-%d %H:%M:%S +0000')
        if item[-3:] == "UTC":
            data[header[i]] = datetime.strptime(item, '%Y-%m-%d %H:%M:%S UTC')

    print data
    print ""


def data_clean(filename):
    for infile in filename:
        outfile = "{file}-{processed}".format(file=infile, processed=config.get("input").get("processed"))
        if os.path.exists(outfile):
            continue
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
                outfile.writerow(row.split("\t"))
                # reformat_data(header, row)


if __name__ == '__main__':
    # this allows us to specify a list of files
    if len(sys.argv) > 1:
        data_clean(sys.argv[1:])
    else:
        data_clean(glob.glob("{path}/*.{extension}".format(**config.get("input"))))
