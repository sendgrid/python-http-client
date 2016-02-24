import time
import os
import json
try:
    # Python 3
    import urllib.request as urllib
    from urllib.parse import urlencode
except ImportError:
    # Python 2
    import urllib2 as urllib
    from urllib import urlencode
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from client import Client
    from config import Config


class StaticClient(Client):
    def __getattr__(self, value):
        self._add_to_url_path(value)
        return self

    def make_request(self, method, data=None, params=None, headers=None):
        method = method.upper()
        if headers:
            self._set_headers(headers)
            data = json.dumps(data) if data else None
            params = params if params else None
            opener = urllib.build_opener()
            request = urllib.Request(self._build_url(params), data=data)
            for key, value in self.request_headers.iteritems():
                request.add_header(key, value)
            request.get_method = lambda: method
            self._response = opener.open(request)
            self._set_response(self._response)
            self._reset()


    def get(self, data=None, params=None, headers=None):
        self._response = self.make_request('get', data, params, headers)
        return self

    def post(self, data=None, params=None, headers=None):
        self._response = self.make_request('post', data, params, headers)
        return self

    def put(self, data=None, params=None, headers=None):
        self._response = self.make_request('put', data, params, headers)
        return self

    def patch(self, data=None, params=None, headers=None):
        self._response = self.make_request('patch', data, params, headers)
        return self

    def delete(self, data=None, params=None, headers=None):
        self._response = self.make_request('delete', data, params, headers)
        return self


# Shout out to Zapier: https://zapier.com/engineering/profiling-python-boss
def timefunc(f):
    def f_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print f.__name__, 'took', end - start, 'seconds'
        return result
    return f_timer


def get_number():
    for x in xrange(5000000):
        yield x


def run_tested_code(client, num_loops):
    while num_loops > 0:
        headers = {'X-Mock': 200}
        params = {'limit': 100}
        response = client.api_keys.get(params=params, headers=headers)

        data = {'sample': 'data'}
        headers = {'X-Mock': 201}
        response = client.api_keys.post(data=data, headers=headers)

        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        api_key_id = "test_url_param"
        response = client.api_keys._(api_key_id).put(data=data,
                                                     headers=headers)

        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        api_key_id = "test_url_param"
        response = client.api_keys._(api_key_id).patch(data=data,
                                                       headers=headers)

        headers = {'X-Mock': 204}
        api_key_id = "test_url_param"
        response = client.api_keys._(api_key_id).delete(headers=headers)

        num_loops -= 1


@timefunc
def dynamic_version():
    headers = {'X-Mock': 200, 'Content-Type': 'application/json'}
    Config.init_environment()
    client = Client(host=os.environ.get('HOST'),
                    api_key=os.environ.get('SENDGRID_API_KEY'),
                    headers=headers)
    run_tested_code(client, 10)


@timefunc
def static_version():
    headers = {'X-Mock': 200, 'Content-Type': 'application/json'}
    Config.init_environment()
    client = StaticClient(host=os.environ.get('HOST'),
                          api_key=os.environ.get('SENDGRID_API_KEY'),
                          headers=headers)
    run_tested_code(client, 10)

dynamic_result = dynamic_version()

static_result = static_version()
