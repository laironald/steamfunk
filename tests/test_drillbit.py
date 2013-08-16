import unittest
import os
import sys

# make this path independent
sys.path.append(os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    ".."))
from lib import drillbit


class TestDrillBit(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_(self):
        pass

if __name__ == '__main__':
    unittest.main()
