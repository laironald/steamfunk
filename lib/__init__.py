import os
import re
import ConfigParser
from collections import defaultdict
from schema import *


def get_config(localfile="config.ini"):
    """
    This grabs a configuration file and converts it into
    a dictionary.

    The default filename is called config.ini
    First we load the global file, then we load a local file
    """

    openfile = "{0}/{1}".format(os.path.dirname(os.path.realpath(__file__)), localfile)
    config = defaultdict(dict)
    if os.path.isfile(openfile):
        cfg = ConfigParser.ConfigParser()
        cfg.read(openfile)
        for s in cfg.sections():
            for k, v in cfg.items(s):
                if v in ("True", "False") or v.isdigit():
                    v = eval(v)
                config[s][k] = v
    return config


def fetch_session():
    config = get_config()
    db = config.get('global').get('database')
    echo = config.get(db).get('echo')

    if db[:6] == "sqlite":
        sqlite_db_path = os.path.join(
            config.get(db).get('path'),
            config.get(db).get('database'))
        engine = create_engine('sqlite:///{0}'.format(sqlite_db_path), echo=echo)
    else:
        engine = create_engine('mysql+mysqldb://{0}:{1}@{2}/{3}?charset=utf8'.format(
            config.get(db).get('user'),
            config.get(db).get('password'),
            config.get(db).get('host'),
            config.get(db).get('database')), echo=echo)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
