[![Travis Badge](https://travis-ci.org/sendgrid/python-http-client.svg?branch=master)](https://travis-ci.org/sendgrid/python-http-client) [![Code Climate](https://codeclimate.com/github/sendgrid/python-http-client/badges/gpa.svg)](https://codeclimate.com/github/sendgrid/python-http-client) [![Coverage Status](https://coveralls.io/repos/github/sendgrid/python-http-client/badge.svg?branch=master)](https://coveralls.io/github/sendgrid/python-http-client?branch=master) [![PyPi Versionse](https://img.shields.io/pypi/pyversions/python-http-client.svg)](https://pypi.python.org/pypi/python-http-client/)

**Quickly and easily access any REST or REST-like API.**

Here is a quick example:

`GET /your/api/{param}/call`

```python
import python_http_client
global_headers = {'Authorization': 'Basic XXXXXXX'}
client = Client(host='base_url', request_headers=global_headers)
client.your.api._(param).call.get()
print response.status_code
print response.response_headers
print response.response_body
```

`POST /your/api/{param}/call` with headers, query parameters and a request body with versioning.

```python
import python_http_client
global_headers = {'Authorization': 'Basic XXXXXXX'}
client = Client(host='base_url', request_headers=global_headers)
query_params={'hello':0, 'world':1}
request_headers={'X-Test': 'test'}
data={'some': 1, 'awesome', 2, 'data', 3}
response = client.your.api._(param).call.post(request_body=data,
                                              query_params=query_params,
                                              request_headers=request_headers)
print response.status_code
print response.response_headers
print response.response_body
```

# Installation

`pip install python_http_client`

or

`easy_install python_http_client`

## Usage ##

Following is an example using SendGrid. You can get your free account [here](https://sendgrid.com/free?source=python-http-client).

First, update your .env with your [SENDGRID_API_KEY](https://app.sendgrid.com/settings/api_keys) and HOST. For this example HOST=https://api.sendgrid.com.

Following is an abridged example, here is the [full working code](https://github.com/sendgrid/python-http-client/tree/master/examples).

```python
import os
import json
import python_http_client
path_to_env = os.path.abspath(os.path.dirname(__file__))
python_http_client.Config(path_to_env)
host = os.environ.get('HOST')
api_key = os.environ.get('SENDGRID_API_KEY')
request_headers = {'Authorization': 'Bearer {0}'.format(api_key), 'Content-Type': 'application/json'}
version = 3 # note that we could also do client.version(3) to set the version for each endpoint
client = python_http_client.Client(host=host,
                                   request_headers=request_headers,
                                   version=version)

# GET collection
response = client.api_keys.get()

# POST
data = {
    "name": "My API Key",
    "scopes": [
        "mail.send",
        "alerts.create",
        "alerts.read"
    ]
}

response = client.api_keys.post(request_body=data)
json_response = json.loads(response.response_body)
api_key_id = json_response['api_key_id']

# GET single
response = client.api_keys._(api_key_id).get()

# PATCH
data = {
    "name": "A New Hope"
}
response = client.api_keys._(api_key_id).patch(request_body=data)

# PUT
data = {
    "name": "A New Hope",
    "scopes": [
        "user.profile.read",
        "user.profile.update"
    ]
}
response = client.api_keys._(api_key_id).put(request_body=data)

# DELETE
response = client.api_keys._(api_key_id).delete()
```

# Announcements

[2016.02.25] - We hit version 1!

# Roadmap

[Milestones](https://github.com/sendgrid/python-http-client/milestones)

# How to Contribute

We encourage contribution to our libraries, please see our [CONTRIBUTING](https://github.com/sendgrid/python-http-client/blob/master/CONTRIBUTING.md) guide for details.

* [Feature Request](https://github.com/sendgrid/python-http-client/blob/master/CONTRIBUTING.md#feature_request)
* [Bug Reports](https://github.com/sendgrid/python-http-client/blob/master/CONTRIBUTING.md#submit_a_bug_report)
* [Improvements to the Codebase](https://github.com/sendgrid/python-http-client/blob/master/CONTRIBUTING.md#improvements_to_the_codebase)

# Thanks

We were inspired by the work done on [birdy](https://github.com/inueni/birdy) and [universalclient](https://github.com/dgreisen/universalclient).

# About

![SendGrid Logo]
(https://assets3.sendgrid.com/mkt/assets/logos_brands/small/sglogo_2015_blue-9c87423c2ff2ff393ebce1ab3bd018a4.png)

python-http-client is guided and supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

python-http-client is maintained and funded by SendGrid, Inc. The names and logos for python-http-client are trademarks of SendGrid, Inc.
