import time
import os
import requests
from functools import wraps
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from client import Client
    from config import Config


class StaticClient(Client):
    def __getattr__(self, value):
        self._add_to_url_path(value)
        return self

    def method_wrapper(func):

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if kwargs['headers']:
                self._set_headers(kwargs['headers'])

            response = func(self, *args, **kwargs)

            self._set_response(self._response)
            self._reset()
            return response

        return wrapper

    def _build_url(self):
        url = ""
        count = 0
        while count < len(self._url_path):
            url += "/" + self._url_path[count]
            count += 1
        return self.host + url

    def _set_response(self, response):
        self._status_code = response.status_code
        self._body = response.text
        self._headers = response.headers

    @method_wrapper
    def get(self, data=None, params=None, headers=None):
        self._response = requests.get(self._build_url(),
                                      params=params,
                                      data=data,
                                      headers=self.request_headers)
        return self

    @method_wrapper
    def post(self, data=None, params=None, headers=None):
        self._response = requests.post(self._build_url(),
                                       params=params,
                                       data=data,
                                       headers=self.request_headers)
        return self

    @method_wrapper
    def put(self, data=None, params=None, headers=None):
        self._response = requests.put(self._build_url(),
                                      params=params,
                                      data=data,
                                      headers=self.request_headers)
        return self

    @method_wrapper
    def patch(self, data=None, params=None, headers=None):
        self._response = requests.patch(self._build_url(),
                                        params=params,
                                        data=data,
                                        headers=self.request_headers)
        return self

    @method_wrapper
    def delete(self, data=None, params=None, headers=None):
        self._response = requests.delete(self._build_url(),
                                         params=params,
                                         data=data,
                                         headers=self.request_headers)
        return self


def timefunc(f):
    def f_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print f.__name__, 'took', end - start, 'time'
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
    client = Client(host=os.environ.get('LOCAL_HOST'),
                    api_key=os.environ.get('SENDGRID_API_KEY'),
                    headers=headers)
    run_tested_code(client, 10)


@timefunc
def static_version():
    headers = {'X-Mock': 200, 'Content-Type': 'application/json'}
    Config.init_environment()
    client = StaticClient(host=os.environ.get('LOCAL_HOST'),
                          api_key=os.environ.get('SENDGRID_API_KEY'),
                          headers=headers)
    run_tested_code(client, 10)

dynamic_result = dynamic_version()

static_result = static_version()
