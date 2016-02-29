"""HTTP Client library"""
import json


try:
    # Python 3
    import urllib.request as urllib
    from urllib.parse import urlencode
except ImportError:
    # Python 2
    import urllib2 as urllib
    from urllib import urlencode


class Client(object):
    """Quickly and easily access any REST or REST-like API."""
    def __init__(self,
                 host,
                 request_headers=None,
                 version=None):
        """
        :param host: Base URL for the api. (e.g. https://api.sendgrid.com)
        :type host:  string
        :param request_headers: A dictionary of the headers you want
                                applied on all calls
        :type request_headers: dictionary
        :param version: The version number of the API.
                        Subclass _build_versioned_url for custom behavior.
                        Or just pass the version as part of the URL
                        (e.g. client._("/v3"))
        :type integer:
        """
        self.host = host
        self.request_headers = request_headers
        # These are the supported HTTP verbs
        self.methods = ['delete', 'get', 'patch', 'post', 'put']
        self._version = version
        # _count and _url_path keep track of the dynamically built url
        self._count = 0
        self._url_path = {}
        self._status_code = None
        self._response_body = None
        self._response_headers = None
        self._response = None

    def _reset(self):
        """Resets the URL builder, so you can make a fresh new dynamic call."""
        self._count = 0
        self._url_path = {}
        self._response = None

    def _add_to_url_path(self, name):
        """Takes the method chained call and adds to the url path.

           :param name: The name of the method call
           :type name: string
        """
        self._url_path[self._count] = name
        self._count += 1

    def _build_versioned_url(self, url):
        """Subclass this function for your own needs.
           Or just pass the version as part of the URL
           (e.g. client._('/v3'))
        :param url: URI portion of the full URL being requested
        :type url: string
        :return:
        """
        return '{0}/v{1}{2}'.format(self.host, str(self._version), url)

    def _build_url(self, query_params):
        """Build the final URL to be passed to urllib

        :param query_params: A dictionary of all the query parameters
        :type query_params: dictionary
        :return:
        """
        url = ''
        count = 0
        while count < len(self._url_path):
            url += '/{0}'.format(self._url_path[count])
            count += 1
        if query_params:
            url_values = urlencode(sorted(query_params.items()))
            url = '{0}?{1}'.format(url, url_values)
        if self._version:
            url = self._build_versioned_url(url)
        else:
            url = self.host + url
        return url

    def _set_response(self, response):
        """Build the API call's response

        :param response: The response object from the API call from urllib
        :type response: urllib.Request object
        """
        self._status_code = response.getcode()
        self._response_body = response.read()
        self._response_headers = response.info()

    def _set_headers(self, request_headers):
        """Build the headers for the request

        :param request_headers: headers to set for the API call
        :type response: dict
        :return:
        """
        if self.request_headers:
            self.request_headers.update(request_headers)
        else:
            self.request_headers = request_headers

    def _make_request(self, opener, request):
        """Make the API call and return the response. This is separated into
           it's own function, so we can mock it easily for testing.

        :param opener:
        :type opener:
        :param request: url payload to request
        :type request: urllib.Request object
        :return:
        """
        return opener.open(request)

    def _(self, name):
        """Add variable values to the url.
           (e.g. /your/api/{variable_value}/call)
           Another example: if you have a Python reserved word, such as global,
           in your url, you must use this method.

        :param name: Name of the url segment
        :type name: string
        :return:
        """
        self._add_to_url_path(name)
        return self

    def __getattr__(self, name):
        """Dynamically add method calls to the url, then call a method.
           (e.g. client.name.name.method())
           You can also add a version number by using .version(<int>)

        :param name: Name of the url segment or method call
        :type name: string or integer if name == version
        :return: mixed
        """
        if name == 'version':
            def get_version(*args, **kwargs):
                """
                :param args: dict of settings
                :param kwargs: unused
                :return: string, version
                """
                self._version = args[0]
                return self
            return get_version

        # We have reached the end of the method chain, make the API call
        if name in self.methods:
            method = name.upper()

            def http_request(*args, **kwargs):
                """Make the API call
                :param args: unused
                :param kwargs:
                :return: Client object
                """
                if 'request_headers' in kwargs:
                    self._set_headers(kwargs['request_headers'])
                data = json.dumps(kwargs['request_body']).encode('utf-8')\
                    if 'request_body' in kwargs else None
                params = kwargs['query_params']\
                    if 'query_params' in kwargs else None
                opener = urllib.build_opener()
                request = urllib.Request(self._build_url(params), data=data)
                if self.request_headers:
                    for key, value in self.request_headers.items():
                        request.add_header(key, value)
                request.get_method = lambda: method
                self._response = self._make_request(opener, request)
                self._set_response(self._response)
                self._reset()
                return self
            return http_request
        else:
            self._add_to_url_path(name)
        return self

    @property
    def status_code(self):
        """
        :return: integer, status code of API call
        """
        return self._status_code

    @property
    def response_body(self):
        """
        :return: response from the API
        """
        return self._response_body

    @property
    def response_headers(self):
        """
        :return: dict of response headers
        """
        return self._response_headers
