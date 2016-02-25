try:
    import unittest2 as unittest
except ImportError:
    import unittest
from python_http_client.config import Config
from python_http_client.client import Client
import os


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


class TestConfig(unittest.TestCase):
    def setUp(self):
        Config()

    def test_initialization(self):
        local_host = os.environ.get('LOCAL_HOST')
        self.assertTrue(isinstance(local_host, basestring))
        host = os.environ.get('HOST')
        self.assertTrue(isinstance(host, basestring))
        sendgrid_api_key = os.environ.get('SENDGRID_API_KEY')
        self.assertTrue(isinstance(sendgrid_api_key, basestring))


class TestClient(unittest.TestCase):
    def setUp(self):
        Config()
        self.api_key = os.environ.get('SENDGRID_API_KEY')
        self.host = os.environ.get('LOCAL_HOST')
        self.request_headers = {'Content-Type': 'application/json'}
        self.client = Client(host=self.host,
                             api_key=self.api_key,
                             request_headers=self.request_headers,
                             version=3)

    def test__init__(self):
        self.assertEqual(os.environ.get('LOCAL_HOST'), self.host)
        authorization = {'Authorization': 'Bearer ' + self.api_key}
        self.request_headers.update(authorization)
        self.assertEqual(self.client.request_headers, self.request_headers)
        methods = ['delete', 'get', 'patch', 'post', 'put']
        self.assertEqual(self.client.methods.sort(), methods.sort())
        self.assertEqual(self.client._version, 3)
        self.assertEqual(self.client._count, 0)
        self.assertEqual(self.client._url_path, {})
        self.assertEqual(self.client._status_code, None)
        self.assertEqual(self.client._response_body, None)
        self.assertEqual(self.client._response_headers, None)
        self.assertEqual(self.client._response, None)

    def test__reset(self):
        self.client._reset()
        self.assertEqual(self.client._count, 0)
        self.assertEqual(self.client._url_path, {})
        self.assertEqual(self.client._response, None)

    def test__add_to_url_path(self):
        self.client._add_to_url_path("here")
        self.client._add_to_url_path("there")
        self.client._add_to_url_path(1)
        self.assertEqual(self.client._count, 3)
        url_path = {0: 'here', 1: 'there', 2: 1}
        self.assertEqual(self.client._url_path, url_path)
        self.client._reset()

    def test__build_versioned_url(self):
        url = "/api_keys?hello=1&world=2"
        versioned_url = self.client._build_versioned_url(url)
        self.assertEqual(versioned_url,
                         self.host + "/v" + str(self.client._version) + url)

    def test__build_url(self):
        self.client._add_to_url_path("here")
        self.client._add_to_url_path("there")
        self.client._add_to_url_path(1)
        query_params = {"hello": 0, "world": 1}
        url = self.host + "/v" + str(self.client._version)\
            + "/here/there/1?hello=0&world=1"
        self.assertEqual(self.client._build_url(query_params), url)
        self.client._reset()

    def test__set_response(self):
        opener = urllib.build_opener()
        self.client._add_to_url_path("api_keys")
        query_params = {"mock": 200}
        request = urllib.Request(self.client._build_url(query_params))
        for key, value in self.client.request_headers.items():
            request.add_header(key, value)
        request.get_method = lambda: 'GET'
        response = opener.open(request)
        self.client._set_response(response)
        self.assertEqual(self.client._status_code, 200)
        self.assertTrue(b'result' in self.client._response_body)
        self.assertTrue(b'name' in self.client._response_body)
        self.assertTrue(b'api_key_id' in self.client._response_body)
        self.assertEqual(self.client._response_headers, response.info())
        self.client._reset()

    def test__set_headers(self):
        request_headers = {"X-Test": "Test"}
        self.client._set_headers(request_headers)
        self.assertTrue("X-Test" in self.client.request_headers)
        self.client.request_headers.pop("X-Test", None)

    def test__(self):
        self.assertEqual(self.client._url_path, {})
        self.client._("hello")
        url_path = {0: 'hello'}
        self.assertEqual(self.client._url_path, url_path)
        self.client._reset()

    def test__getattr__(self):
        self.client.__getattr__("hello")
        url_path = {0: 'hello'}
        self.assertEqual(self.client._url_path, url_path)
        self.assertEqual(self.client.__getattr__("get").__name__,
                         "http_request")
        self.client._reset()

        # Test Version
        self.client.version(3)
        self.assertEqual(self.client._version, 3)

        # Test GET
        self.client.request_headers.update({'X-Mock': 200})
        self.client._add_to_url_path("api_keys")
        self.client.get()
        self.assertEqual(self.client.status_code, 200)

        # Test POST
        self.client.request_headers.update({'X-Mock': 200})
        self.client._add_to_url_path("api_keys")
        self.client._add_to_url_path("api_key_id")
        self.client.put()
        self.assertEqual(self.client.status_code, 200)

        # Test PATCH
        self.client.request_headers.update({'X-Mock': 200})
        self.client._add_to_url_path("api_keys")
        self.client._add_to_url_path("api_key_id")
        self.client.patch()
        self.assertEqual(self.client.status_code, 200)

        # Test POST
        self.client.request_headers.update({'X-Mock': 201})
        self.client._add_to_url_path("api_keys")
        self.client.post()
        self.assertEqual(self.client.status_code, 201)

        # Test DELETE
        self.client._add_to_url_path("api_keys")
        self.client._add_to_url_path("api_key_id")
        self.client.request_headers.update({'X-Mock': 204})
        self.client.delete()
        self.assertEqual(self.client.status_code, 204)

        self.client._reset()

if __name__ == '__main__':
    unittest.main()
