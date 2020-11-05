import time
import os
import json

try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from python_http_client.client import Client
    from python_http_client.config import Config


class StaticClient(Client):
    def __getattr__(self, value):
        """
        Get the value of the given attribute.

        Args:
            self: (todo): write your description
            value: (str): write your description
        """
        self._add_to_url_path(value)
        return self

    def make_request(self,
                     method,
                     request_body=None,
                     query_params=None,
                     request_headers=None):
        """
        Make an http request.

        Args:
            self: (todo): write your description
            method: (str): write your description
            request_body: (str): write your description
            query_params: (dict): write your description
            request_headers: (todo): write your description
        """
        method = method.upper()
        if request_headers:
            self._set_headers(request_headers)
            request_body = json.dumps(request_body) if request_body else None
            query_params = query_params if query_params else None
            opener = urllib.build_opener()
            request = urllib.Request(self._build_url(query_params),
                                     data=request_body)
            for key, value in self.request_headers.iteritems():
                request.add_header(key, value)
            request.get_method = lambda: method
            self._response = opener.open(request)
            self._set_response(self._response)
            self._reset()

    def get(self,
            request_body=None,
            query_params=None,
            request_headers=None):
        """
        Perform a get request.

        Args:
            self: (todo): write your description
            request_body: (str): write your description
            query_params: (dict): write your description
            request_headers: (str): write your description
        """
        self.make_request('get', request_body, query_params,
                          request_headers)
        return self

    def post(self,
             request_body=None,
             query_params=None,
             request_headers=None):
        """
        Make a post request.

        Args:
            self: (todo): write your description
            request_body: (str): write your description
            query_params: (dict): write your description
            request_headers: (str): write your description
        """
        self.make_request('post', request_body, query_params,
                          request_headers)
        return self

    def put(self,
            request_body=None,
            query_params=None,
            request_headers=None):
        """
        Perform a put request.

        Args:
            self: (todo): write your description
            request_body: (str): write your description
            query_params: (dict): write your description
            request_headers: (todo): write your description
        """
        self.make_request('put', request_body, query_params,
                          request_headers)
        return self

    def patch(self,
              request_body=None,
              query_params=None,
              request_headers=None):
        """
        Perform a patch request.

        Args:
            self: (todo): write your description
            request_body: (todo): write your description
            query_params: (dict): write your description
            request_headers: (str): write your description
        """
        self.make_request('patch', request_body, query_params,
                          request_headers)
        return self

    def delete(self,
               request_body=None,
               query_params=None,
               request_headers=None):
        """
        Make a delete request.

        Args:
            self: (todo): write your description
            request_body: (str): write your description
            query_params: (dict): write your description
            request_headers: (str): write your description
        """
        self.make_request('delete', request_body, query_params,
                          request_headers)
        return self


# Shout out to Zapier: https://zapier.com/engineering/profiling-python-boss
def timefunc(f):
    """
    Decorator to log execution.

    Args:
        f: (todo): write your description
    """
    def f_timer(*args, **kwargs):
        """
        Decorator to execute a function.

        Args:
        """
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f.__name__, 'took', end - start, 'seconds')
        return result
    return f_timer


def get_number():
    """
    Get the number from the number.

    Args:
    """
    for x in xrange(5000000):
        yield x


def run_tested_code(client, num_loops):
    """
    Run a success return code for a given client.

    Args:
        client: (todo): write your description
        num_loops: (int): write your description
    """
    while num_loops > 0:
        request_headers = {'X-Mock': 200}
        query_params = {'limit': 100}
        client.api_keys.get(query_params=query_params,
                            request_headers=request_headers)

        data = {'sample': 'data'}
        headers = {'X-Mock': 201}
        client.api_keys.post(request_body=data,
                             request_headers=headers)

        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        api_key_id = 'test_url_param'
        client.api_keys._(api_key_id).put(request_body=data,
                                          request_headers=headers)

        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        api_key_id = 'test_url_param'
        client.api_keys._(api_key_id).patch(request_body=data,
                                            request_headers=headers)

        headers = {'X-Mock': 204}
        api_key_id = 'test_url_param'
        client.api_keys._(api_key_id).delete(request_headers=headers)

        num_loops -= 1


@timefunc
def dynamic_version():
    """
    Create dynamic dynamic dynamic dynamic dynamic version.

    Args:
    """
    local_path = '{}/..'.format(os.path.abspath(os.path.dirname(__file__)))
    Config(local_path)
    api_key = os.environ.get('SENDGRID_API_KEY')
    request_headers = {
        'X-Mock': 200,
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(api_key)
    }
    client = Client(host=os.environ.get('LOCAL_HOST'),
                    request_headers=request_headers,
                    version=3)
    run_tested_code(client, 10)


@timefunc
def static_version():
    """
    Create a static version.

    Args:
    """
    local_path = '{}/..'.format(os.path.abspath(os.path.dirname(__file__)))
    Config(local_path)
    api_key = os.environ.get('SENDGRID_API_KEY')
    request_headers = {
        'X-Mock': 200,
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(api_key)
    }
    client = StaticClient(host=os.environ.get('LOCAL_HOST'),
                          request_headers=request_headers,
                          version=3)
    run_tested_code(client, 10)


dynamic_version()
static_version()
