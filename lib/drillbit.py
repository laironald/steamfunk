import urllib
import urllib2
import random
import json
import lib

config = lib.get_config()


def drill(data):
    data.update(config.get("drillbit"))
    req = urllib2.Request("https://drillbitapp.com/api", urllib.urlencode(data))
    res = urllib2.urlopen(req)
    return json.loads(res.read())


def retrieve_names(name):
    if type(name).__name__ == "User":
        return [name.name_first, name.name_last]
    else:
        return name


def prep_names(names, sample=1000, seed=20130812):
    firstnames = []
    lastnames = []
    if type(names).__name__ == "Query":
        names = names.filter(lib.User.name_first is not None)
        size = names.count()
    elif type(names).__name__ in ("list", "tuple"):
        size = len(names)

    random.seed(seed)
    # we do this if sampling makes sense
    if sample and size > sample:
        print size, sample
        samp = random.sample(xrange(size), sample)
    else:
        samp = None

    for i, name in enumerate(names):
        if samp and i not in samp:
            continue
        name = retrieve_names(name)
        firstnames.append(name[0])
        lastnames.append(name[1])

    return {
        "firstnames": ",".join(firstnames),
        "lastnames":  ",".join(lastnames)
    }
