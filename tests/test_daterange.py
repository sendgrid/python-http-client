import os
import time

try:
    import unittest2 as unittest
except ImportError:
    import unittest


class DateRangeTest(unittest.TestCase):
    def setUp(self):
        self.openlicensefile = os.path.join(
                                os.path.dirname(__file__),
                                '../LICENSE.txt')
        self.pattern = 'Copyright (c) 2012 - %s SendGrid, Inc.' % (
                        time.strftime("%Y"))
        self.licensefile = open(self.openlicensefile).read()

    def test__daterange(self):
        self.assertTrue(self.pattern in self.licensefile)
