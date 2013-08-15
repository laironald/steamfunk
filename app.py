import glob
import sys
import lib
import os


config = lib.get_config()


def data_clean(filename):
    for infile in filename:
        outfile = "{file}-{processed}".format(file=infile, processed=config.get("input").get("processed"))
        if os.path.exists(outfile):
            continue
        infile = open(infile, "rb")
        outfile = open(outfile, "wb")


if __name__ == '__main__':
    # this allows us to specify a list of files
    if len(sys.argv) > 1:
        data_clean(sys.argv[1:])
    else:
        data_clean(glob.glob("{path}/*.{extension}".format(**config.get("input"))))
