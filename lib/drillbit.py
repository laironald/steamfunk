import urllib
import urllib2
import json


def drill(data):
    data.update(config.get("drillbit"))
    req = urllib2.Request("https://drillbitapp.com/api", urllib.urlencode(data))
    res = urllib2.urlopen(req)
    return json.loads(res.read())

