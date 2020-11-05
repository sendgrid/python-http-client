import pickle
import unittest

from python_http_client.client import Client, HTTPError, urllib
from python_http_client.exceptions import (
    HTTPError as SG_HTTPError,
    BadRequestsError,
    NotFoundError,
    ServiceUnavailableError,
    UnsupportedMediaTypeError,
)

try:
    # Python 3
    from unittest import mock
except ImportError:
    # Python 2
    import mock

try:
    basestring
except NameError:
    basestring = str


class MockException(HTTPError):

    def __init__(self, url, response_code):
        """
        Çļ»å½ķ

        Args:
            self: (todo): write your description
            url: (str): write your description
            response_code: (todo): write your description
        """
        super(MockException, self).__init__(
            url, response_code, 'REASON', 'HEADERS', None
        )

    def read(self):
        """
        Reads the next to readme.

        Args:
            self: (todo): write your description
        """
        return 'BODY'


class MockResponse(urllib.HTTPSHandler):

    def __init__(self, response_code):
        """
        Initialize the response.

        Args:
            self: (todo): write your description
            response_code: (todo): write your description
        """
        self.response_code = response_code

    def getcode(self):
        """
        Get the response code.

        Args:
            self: (todo): write your description
        """
        return self.response_code

    def info(self):
        """
        Returns the info as a string.

        Args:
            self: (todo): write your description
        """
        return 'HEADERS'

    def read(self):
        """
        Reads the next to readme.

        Args:
            self: (todo): write your description
        """
        return 'RESPONSE BODY'


class MockOpener:

    def __init__(self):
        """
        Initialize the response.

        Args:
            self: (todo): write your description
        """
        self.response_code = 200

    def open(self, request, timeout=None):
        """
        Open a response object.

        Args:
            self: (todo): write your description
            request: (todo): write your description
            timeout: (float): write your description
        """
        if 200 <= self.response_code < 299:  # if successful code
            return MockResponse(self.response_code)
        else:
            raise MockException(request.get_full_url(), self.response_code)


class TestClient(unittest.TestCase):

    def setUp(self):
        """
        Sets the client headers

        Args:
            self: (todo): write your description
        """
        self.host = 'http://api.test.com'
        self.api_key = "SENDGRID_API_KEY"
        self.request_headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.api_key)
        }
        self.client = Client(host=self.host,
                             request_headers=self.request_headers,
                             version=3)

    def test__init__(self):
        """
        Initialize the connection.

        Args:
            self: (todo): write your description
        """
        default_client = Client(host=self.host)
        self.assertEqual(default_client.host, self.host)
        self.assertEqual(default_client.request_headers, {})
        self.assertIs(default_client.timeout, None)
        methods = {'delete', 'get', 'patch', 'post', 'put'}
        self.assertEqual(default_client.methods, methods)
        self.assertIsNone(default_client._version)
        self.assertEqual(default_client._url_path, [])

        request_headers = {'X-Test': 'test', 'X-Test2': 1}
        version = 3
        client = Client(host=self.host,
                        request_headers=request_headers,
                        version=version,
                        timeout=10)
        self.assertEqual(client.host, self.host)
        self.assertEqual(client.request_headers, request_headers)
        methods = {'delete', 'get', 'patch', 'post', 'put'}
        self.assertEqual(client.methods, methods)
        self.assertEqual(client._version, 3)
        self.assertEqual(client._url_path, [])
        self.assertEqual(client.timeout, 10)

    def test__build_versioned_url(self):
        """
        Build the urled urled test url.

        Args:
            self: (todo): write your description
        """
        url = '/api_keys?hello=1&world=2'
        versioned_url = self.client._build_versioned_url(url)
        url = '{}/v{}{}'.format(self.host, str(self.client._version), url)
        self.assertEqual(versioned_url, url)

    def test__build_url(self):
        """
        Constructs the url for this build.

        Args:
            self: (todo): write your description
        """
        self.client._url_path = self.client._url_path + ['here']
        self.client._url_path = self.client._url_path + ['there']
        self.client._url_path = self.client._url_path + [1]
        self.client._version = 3
        url = '{}/v{}{}'.format(
            self.host,
            str(self.client._version),
            '/here/there/1?hello=0&world=1&ztest=0&ztest=1'
        )
        query_params = {'hello': 0, 'world': 1, 'ztest': [0, 1]}
        built_url = self.client._build_url(query_params)
        self.assertEqual(built_url, url)

    @mock.patch('python_http_client.client.Client._make_request')
    def test__urllib_headers(self, maker):
        """
        : return : dict of headers

        Args:
            self: (todo): write your description
            maker: (str): write your description
        """
        self.client._update_headers({'X-test': 'Test'})
        self.client.get()
        request = maker.call_args[0][1]
        self.assertIn('X-test', request.headers)

    @mock.patch('python_http_client.client.Client._make_request')
    def test__urllib_method(self, maker):
        """
        Test if the test method.

        Args:
            self: (todo): write your description
            maker: (todo): write your description
        """
        self.client.delete()
        request = maker.call_args[0][1]
        self.assertEqual(request.get_method(), 'DELETE')

    def test__update_headers(self):
        """
        Updates headers.

        Args:
            self: (todo): write your description
        """
        request_headers = {'X-Test': 'Test'}
        self.client._update_headers(request_headers)
        self.assertIn('X-Test', self.client.request_headers)
        self.client.request_headers.pop('X-Test', None)

    def test__build_client(self):
        """
        Create a new client.

        Args:
            self: (todo): write your description
        """
        new_client = self.client._build_client('test')
        self.assertTrue(new_client)

    def test__(self):
        """
        Gets the test configuration.

        Args:
            self: (todo): write your description
        """
        self.assertEqual(self.client._url_path, [])
        client = self.client._('hello')
        url_path = ['hello']
        self.assertEqual(client._url_path[0], url_path[0])

    @mock.patch('python_http_client.client.urllib')
    def test__getattr__(self, mock_lib):
        """
        Test for a mock for a mock.

        Args:
            self: (todo): write your description
            mock_lib: (str): write your description
        """
        mock_opener = MockOpener()
        mock_lib.build_opener.return_value = mock_opener

        client = self.client.__getattr__('hello')
        url_path = ['hello']
        self.assertEqual(client._url_path, url_path)
        self.assertEqual(client.__getattr__('get').__name__, 'http_request')

        # Test Version
        client.version(3)
        self.assertEqual(client._version, 3)

        # Test GET
        client._url_path += ['test']
        r = client.get()
        self.assertEqual(r.status_code, 200)

        # Test POST
        r = client.put()
        self.assertEqual(r.status_code, 200)

        # Test PATCH
        r = client.patch()
        self.assertEqual(r.status_code, 200)

        # Test POST
        mock_opener.response_code = 201
        r = client.post()
        self.assertEqual(r.status_code, 201)

        # Test DELETE
        mock_opener.response_code = 204
        r = client.delete()
        self.assertEqual(r.status_code, 204)

        mock_opener.response_code = 400
        self.assertRaises(BadRequestsError, client.get)

        mock_opener.response_code = 404
        self.assertRaises(NotFoundError, client.post)

        mock_opener.response_code = 415
        self.assertRaises(UnsupportedMediaTypeError, client.patch)

        mock_opener.response_code = 503
        self.assertRaises(ServiceUnavailableError, client.delete)

        mock_opener.response_code = 523
        self.assertRaises(SG_HTTPError, client.delete)

    def test_client_pickle_unpickle(self):
        """
        Test if client pickle client.

        Args:
            self: (todo): write your description
        """
        pickled_client = pickle.dumps(self.client)
        unpickled_client = pickle.loads(pickled_client)
        self.assertDictEqual(
            self.client.__dict__,
            unpickled_client.__dict__,
            "original client and unpickled client must have the same state"
        )


if __name__ == '__main__':
    unittest.main()
