import unittest
import os
import sys

# make this path independent
sys.path.append(os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    ".."))
import lib
from lib import drillbit


class TestDrillBit(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_drill(self):
        data = {"firstnames": "Darling", "lastnames": "Sanders"}
        self.assertItemsEqual(
            [u'skippedLastNames', u'gender', u'age', u'skippedFirstNames', u'totalLastNames', u'race', u'matchedFirstNames', u'matchedLastNames', u'totalFirstNames'],
            drillbit.drill(data).keys())

    def test_retrieve_names(self):
        # passing in the User class
        user = lib.session.query(lib.User).filter(lib.User.id == '137').first()
        self.assertItemsEqual(
            [u'Jesse', u'Yates'],
            drillbit.retrieve_names(user))

        # passing in User parsed by first/last
        user = lib.session.query(lib.User.name_first, lib.User.name_last).filter(lib.User.id == '137').first()
        self.assertItemsEqual(
            [u'Jesse', u'Yates'],
            drillbit.retrieve_names(user))

        # passing in an array
        user = ["Todd", "Silverstein"]
        self.assertItemsEqual(
            [u'Todd', u'Silverstein'],
            drillbit.retrieve_names(user))

    def test_prep_names(self):
        names = lib.session.query(lib.User).limit(100)
        self.assertEquals(
            {'lastnames': u'Case,Jivraj,Samsin,TenAas,McMiam,Seid,Garella,Rowan,Spong', 'firstnames': u'Amber,Ahmad,Kim,Grecia,Max,David,Luigi,Mike,Christopher'},
            drillbit.prep_names(names, sample=10, seed=5))

        names = lib.session.query(lib.User)
        self.assertEquals(
            {'lastnames': u'bull,D.,a,Ganadero,Stawecki,a,Papiol', 'firstnames': u'toby,Pedro,Cande,Software,Tomasz,ND>>NNDoDdeg,Jordi'},
            drillbit.prep_names(names, sample=10, seed=5))


if __name__ == '__main__':
    unittest.main()
