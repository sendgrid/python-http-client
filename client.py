import json
import encodings.idna


try:
    import urllib.request as urllib #for python 3
    from urllib.parse import urlencode
except ImportError:
    import urllib2 as urllib # for python 2
    from urllib import urlencode


class Client(object):

    def __init__(self, host=None, api_key=None, headers=None):
        self.host = host
        self.request_headers = {'Authorization': 'Bearer ' + api_key, 'Content-Type': 'application/json'}
        self.methods = ['delete', 'get', 'patch', 'post', 'put']
        if headers:
            self._set_headers(headers)
        self._count = 0
        self._url_path = {}
        self._status_code = None
        self._body = None
        self._response_headers = None
        self._response = None

    def _reset(self):
        self._count = 0
        self._url_path = {}
        self._response = None

    def _add_to_url_path(self, value):
        self._url_path[self._count] = value
        self._count += 1

    def _build_url(self, params):
        url = ""
        count = 0
        while count < len(self._url_path):
            url += "/" + self._url_path[count]
            count += 1
        if params:
            url_values = urlencode(params)
            url = url + '?' + url_values
        return self.host + url

    def _set_response(self, response):
        self._status_code = response.getcode()
        self._body = response.read()
        self._response_headers = response.info()

    def _set_headers(self, headers):
        self.request_headers.update(headers)

    def _(self, value):
        self._add_to_url_path(value)
        return self

    def __getattr__(self, value):
        if value in self.methods:
            method = value.upper()
            def http_request(*args, **kwargs):
                if 'headers' in kwargs:
                    self._set_headers(kwargs['headers'])
                data = json.dumps(kwargs['data']) if 'data' in kwargs else None
                params = kwargs['params'] if 'params' in kwargs else None
                opener = urllib.build_opener()
                request = urllib.Request(self._build_url(params), data=data)  
                for key, value in self.request_headers.iteritems():
                    request.add_header(key, value)
                request.get_method = lambda: method
                self._response = opener.open(request)
                self._set_response(self._response)
                self._reset()
                return self
            return http_request
        else:
            self._add_to_url_path(value)
        return self

    @property
    def status_code(self):
        return self._status_code

    @property
    def body(self):
        return self._body

    @property
    def headers(self):
        return self._response_headers