import os
import time
import unittest
import warnings


class DateRangeTest(unittest.TestCase):
    def setUp(self):
        """
        Sets the license

        Args:
            self: (todo): write your description
        """
        self.openlicensefile = os.path.join(
                                os.path.dirname(__file__),
                                '../LICENSE')
        self.pattern = 'Copyright (C) %s, Twilio SendGrid, Inc.' % (
                        time.strftime("%Y"))
        fh = open(self.openlicensefile)
        self.license_file = fh.read()
        fh.close()

    def test__daterange(self):
        """
        Test if the given pattern.

        Args:
            self: (todo): write your description
        """
        self.assertIn(self.pattern, self.license_file)
