import os
import json
import python_http_client

host = "https://api.sendgrid.com"
api_key = os.environ.get('SENDGRID_API_KEY')
request_headers = {
    "Authorization": 'Bearer {0}'.format(api_key)
}
version = 3  # we could also use client.version(3)
client = python_http_client.Client(host=host,
    request_headers=request_headers, version=version)

# GET collection
response = client.api_keys.get()
print(response.status_code)
print(response.headers)
print(response.body)

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
print(response.status_code)
print(response.headers)
print(response.body)
json_response = json.loads(response.body)
api_key_id = json_response['api_key_id']

# GET single
response = client.api_keys._(api_key_id).get()
print(response.status_code)
print(response.headers)
print(response.body)

# PATCH
data = {
    "name": "A New Hope"
}
response = client.api_keys._(api_key_id).patch(request_body=data)
print(response.status_code)
print(response.headers)
print(response.body)

# PUT
data = {
    "name": "A New Hope",
    "scopes": [
        "user.profile.read",
        "user.profile.update"
    ]
}
response = client.api_keys._(api_key_id).put(request_body=data)
print(response.status_code)
print(response.headers)
print(response.body)

# DELETE
response = client.api_keys._(api_key_id).delete()
print(response.status_code)
print(response.headers)
