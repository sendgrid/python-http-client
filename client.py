import requests
try:
    import urllib.request as urllib #for python 3
except ImportError:
    import urllib2 as urllib # for python 2


class Client(object):

    def __init__(self, host=None, api_key=None, headers=None):
        self.host = host
        self.request_headers = {'Authorization': 'Bearer ' + api_key}
        self.methods = ['get', 'post', 'put', 'patch', 'delete']
        if headers:
            self._set_headers(headers)
        self._count = 0
        self._cache = {}
        self._status_code = None
        self._body = None
        self._headers = None
        self._response = None

    def _reset(self):
        self._count = 0
        self._cache = {}
        self._response = None

    def _add_to_cache(self, value):
        self._cache[self._count] = value
        self._count += 1

    def _build_url(self):
        url = ""
        count = 0
        while count < len(self._cache):
            url += "/" + self._cache[count]
            count += 1
        return self.host + url

    def _set_response(self, response):
        self._status_code = response.status_code
        self._body = response.text
        self._headers = response.headers

    def _set_headers(self, headers):
        self.request_headers.update(headers)

    def _(self, value):
        self._add_to_cache(value)
        return self

    def __getattr__(self, value):
        if value in self.methods:
            def http_request(*args, **kwargs):
                request = getattr(requests, value)
                try:
                    self._set_headers(kwargs['headers'])
                except KeyError:
                    pass
                try:
                    data = kwargs['data']
                except KeyError:
                    data = None
                try:
                    params = kwargs['params']
                except KeyError:
                    params = None                
                self._response = request(self._build_url(),
                                         data=data,
                                         params=params,
                                         headers=self.request_headers)
                self._set_response(self._response)
                self._reset()
                return self
            return http_request
        else:
            self._add_to_cache(value)
        return self

    @property
    def status_code(self):
        return self._status_code

    @property
    def body(self):
        return self._body

    @property
    def headers(self):
        return self._headers