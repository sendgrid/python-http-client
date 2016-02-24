try:
    import unittest2 as unittest
except ImportError:
    import unittest
from config import Config
from client import Client
import os


try:
    basestring
except NameError:
    basestring = str


class TestConfig(unittest.TestCase):
    def setUp(self):
        self.config = Config()

    def test_initialization(self):
        host = os.environ.get('HOST')
        self.assertTrue(isinstance(host, basestring))
        sendgrid_api_key = os.environ.get('SENDGRID_API_KEY')
        self.assertTrue(isinstance(sendgrid_api_key, basestring))


class TestClient(unittest.TestCase):
    def setUp(self):
        Config.init_environment()
        headers = {'X-Mock': 200, 'Content-Type': 'application/json'}
        self.client = Client(host=os.environ.get('HOST'),
                             api_key=os.environ.get('SENDGRID_API_KEY'),
                             headers=headers)

    def test__reset(self):
        self.client._reset()
        self.assertEqual(self.client._count, 0)
        self.assertEqual(self.client._url_path, {})
        self.assertEqual(self.client._response, None)

if __name__ == '__main__':
    unittest.main()