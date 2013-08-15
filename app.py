import glob
import sys
import lib


config = lib.get_config()


def data_clean(filename):
    print filename
    pass


if __name__ == '__main__':
    # this allows us to specify a list of files
    if len(sys.argv) > 1:
        data_clean(sys.argv[1:])
    else:
        data_clean(glob.glob("{path}/*.{extension}".format(**config.get("input"))))
