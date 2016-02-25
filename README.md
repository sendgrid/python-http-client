Quickly and easily access any REST or REST-like API.

Here is a quick example:

GET /your/api/{param}/call

```
import python-http-client
client = Client(host='base_url', api_key='api_key')
client.your.api._(param).call.get()
print response.status_code
print response.response_headers
print response.body 
```

POST /your/api/{param}/call with headers, query params and data, with versioning

```
import python-http-client
global_headers = {'X-Default': 'default'}
client = Client(host='base_url', api_key='api_key', request_headers=global_headers )
query_params={'hello':0, 'world':1}
request_headers={'X-Test': 'test'}
data={'some': 1, 'awesome', 2, 'data', 3}
response = client.your.api._(param).call.post(data=data,
                                              query_params=query_params,
                                              request_headers=request_headers)
print response.status_code
print response.response_headers
print response.body 
```

<<Travis Badge Placeholder>> <<CodeClimate Badge Placeholder>> <<Python Badge Placeholder>>

# Installation

pip install sendgrid
# or
easy_install sendgrid

## Usage ##

Following is an example using SendGrid. You can get your free account [here](https://sendgrid.com).

First, update your .env with your [SENDGRID_API_KEY](https://app.sendgrid.com/settings/api_keys) and HOST. For this example HOST=https://api.sendgrid.com.

Following is an abridged example, here is the [full working code](https://github.com/sendgrid/python-http-client/tree/master/examples).

```
import os
import json
import python-http-client
Config()
host = os.environ.get('HOST')
api_key = os.environ.get('SENDGRID_API_KEY')
request_headers = {'Content-Type': 'application/json'}
version = 3 # note that we could also do client.version(3) to set the version for each endpoint
client = Client(host=host,
                api_key=api_key,
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
response = client.api_keys.post(data=data)
json_response = json.loads(response.body)
api_key_id = json_response['api_key_id']

# GET single
response = client.api_keys._(api_key_id).get()

# PATCH
data = {
          "name": "A New Hope"
        }
response = client.api_keys._(api_key_id).patch(data=data)

# PUT
data = {
          "name": "A New Hope",
          "scopes": [
            "user.profile.read",
            "user.profile.update"
          ]
        }
response = client.api_keys._(api_key_id).put(data=data)

# DELETE
response = client.api_keys._(api_key_id).delete()
```

# Announcements

[2016.02.25] - We hit version 1!

# Roadmap

[Milestones](https://github.com/sendgrid/python-http-client/milestones)

# How to Contribute

We encourage contribution to our libraries, please see our [CONTRIBUTING](https://github.com/sendgrid/python-http-client/blob/master/CONTRIBUTING.md) guide for details.

# About

![SendGrid Logo]
(https://assets3.sendgrid.com/mkt/assets/logos_brands/small/sglogo_2015_blue-9c87423c2ff2ff393ebce1ab3bd018a4.png)

python-http-client is guided and supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

python-http-client is maintained and funded by SendGrid, inc. The names and logos for python-http-client are trademarks of SendGrid, inc.

