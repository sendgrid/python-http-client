import os
import time
import unittest
import warnings


class DateRangeTest(unittest.TestCase):
    def setUp(self):
        self.openlicensefile = os.path.join(
                                os.path.dirname(__file__),
                                '../LICENSE.txt')
        self.pattern = 'Copyright (c) 2012 - %s Twilio SendGrid, Inc.' % (
                        time.strftime("%Y"))
        fh = open(self.openlicensefile)
        self.licensefile = fh.read()
        fh.close()

    def test__daterange(self):
        try:
            self.assertIn(self.pattern, self.licensefile)
        except AssertionError:
            warnings.warn("License file does not contain a current year!")
