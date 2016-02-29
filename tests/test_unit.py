import os
from os import path
try:
    import unittest2 as unittest
except ImportError:
    import unittest
from python_http_client.config import Config
from python_http_client.client import Client


try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib


try:
    basestring
except NameError:
    basestring = str


class MockResponse(urllib.HTTPSHandler):

    def __init__(self, response_code):
        self.response_code = response_code

    def getcode(self):
        return self.response_code

    def info(self):
        return 'HEADERS'

    def read(self):
        return 'RESPONSE BODY'


class MockClient(Client):

    def __init__(self, host, response_code):
        self.response_code = 200
        Client.__init__(self, host)

    def _make_request(self, opener, request):
        return MockResponse(self.response_code)


class TestConfig(unittest.TestCase):
    def test_initialization(self):
        """Make sure your configuration is setup correctly.
           At a minimum, we need a HOST to be defined in .env
           to test the configuration module.
        """
        local_path = os.path.dirname(path.dirname(path.abspath(__file__)))
        config = Config(local_path)
        self.assertEqual(config.local_path_to_env,
                         '{0}/.env'.format(local_path))


class TestClient(unittest.TestCase):
    def setUp(self):
        self.host = 'http://api.test.com'
        self.client = Client(host=self.host)
        if os.environ.get('TRAVIS'):
            Config(os.path.abspath(os.path.dirname(__file__)))
        else:
            local_path = '{0}/..'\
                .format(os.path.abspath(os.path.dirname(__file__)))
            Config(local_path)
        self.api_key = os.environ.get('SENDGRID_API_KEY')
        self.host = os.environ.get('MOCK_HOST')
        self.request_headers = {
                                 'Content-Type': 'application/json',
                                 'Authorization': 'Bearer ' + self.api_key
                                }
        self.client = Client(host=self.host,
                             request_headers=self.request_headers,
                             version=3)

    def test__init__(self):
        default_client = Client(host=self.host)
        self.assertEqual(default_client.host, self.host)
        self.assertEqual(default_client.request_headers, None)
        methods = ['delete', 'get', 'patch', 'post', 'put']
        self.assertEqual(default_client.methods, methods)
        self.assertEqual(default_client._version, None)
        self.assertEqual(default_client._count, 0)
        self.assertEqual(default_client._url_path, {})
        self.assertEqual(default_client._status_code, None)
        self.assertEqual(default_client._response_body, None)
        self.assertEqual(default_client._response_headers, None)
        self.assertEqual(default_client._response, None)

        request_headers = {'X-Test': 'test', 'X-Test2': 1}
        version = 3
        client = Client(host=self.host,
                        request_headers=request_headers,
                        version=version)
        self.assertEqual(client.host, self.host)
        self.assertEqual(client.request_headers, request_headers)
        methods = ['delete', 'get', 'patch', 'post', 'put']
        self.assertEqual(client.methods, methods)
        self.assertEqual(client._version, 3)
        self.assertEqual(client._count, 0)
        self.assertEqual(client._url_path, {})
        self.assertEqual(client._status_code, None)
        self.assertEqual(client._response_body, None)
        self.assertEqual(client._response_headers, None)
        self.assertEqual(client._response, None)

    def test__reset(self):
        self.client._count = 1
        self.client._url_path = {0: 'test', 1: 'path'}
        self.client._response = 'fake_response_object'
        self.client._reset()
        self.assertEqual(self.client._count, 0)
        self.assertEqual(self.client._url_path, {})
        self.assertEqual(self.client._response, None)

    def test__add_to_url_path(self):
        self.client._add_to_url_path("here")
        self.client._add_to_url_path("there")
        self.client._add_to_url_path(str(1))
        self.assertEqual(self.client._count, 3)
        url_path = {0: 'here', 1: 'there', 2: '1'}
        self.assertEqual(self.client._url_path, url_path)
        self.client._reset()

    def test__build_versioned_url(self):
        url = '/api_keys?hello=1&world=2'
        versioned_url = self.client._build_versioned_url(url)
        url = '{0}/v{1}{2}'.format(self.host, str(self.client._version), url)
        self.assertEqual(versioned_url, url)

    def test__build_url(self):
        self.client._add_to_url_path('here')
        self.client._add_to_url_path('there')
        self.client._add_to_url_path(1)
        self.client._version = 3
        url = '{0}/v{1}{2}'.format(self.host,
                                   str(self.client._version),
                                   '/here/there/1?hello=0&world=1')
        query_params = {'hello': 0, 'world': 1}
        built_url = self.client._build_url(query_params)
        self.assertEqual(built_url, url)
        self.client._reset()

    def test__set_response(self):
        response = MockResponse(200)
        self.client._set_response(response)
        self.assertEqual(self.client._status_code, 200)
        self.assertEqual(self.client._response_body, 'RESPONSE BODY')
        self.assertEqual(self.client._response_headers, 'HEADERS')

    def test__set_headers(self):
        request_headers = {'X-Test': 'Test'}
        self.client._set_headers(request_headers)
        self.assertTrue('X-Test' in self.client.request_headers)
        self.client.request_headers.pop('X-Test', None)

    def test__(self):
        self.assertEqual(self.client._url_path, {})
        self.client._("hello")
        url_path = {0: 'hello'}
        self.assertEqual(self.client._url_path, url_path)
        self.client._reset()

    def test__getattr__(self):
        client = MockClient(self.host, 200)
        client.__getattr__('hello')
        url_path = {0: 'hello'}
        self.assertEqual(client._url_path, url_path)
        self.assertEqual(client.__getattr__('get').__name__,
                         'http_request')
        client._reset()

        # Test Version
        client.version(3)
        self.assertEqual(client._version, 3)

        # Test GET
        client._add_to_url_path('test')
        client.get()
        self.assertEqual(client.status_code, 200)

        # Test POST
        client.put()
        self.assertEqual(client.status_code, 200)

        # Test PATCH
        client.patch()
        self.assertEqual(client.status_code, 200)

        # Test POST
        client.response_code = 201
        client.post()
        self.assertEqual(client.status_code, 201)

        # Test DELETE
        client.response_code = 204
        client.delete()
        self.assertEqual(client.status_code, 204)


if __name__ == '__main__':
    unittest.main()
