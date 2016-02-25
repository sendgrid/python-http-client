import os
import json
import python_http_client
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
print response.response_headers
print response.status_code
print response.response_body

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
print response.response_headers
print response.status_code
print response.response_body
json_response = json.loads(response.response_body)
api_key_id = json_response['api_key_id']

# GET single
response = client.api_keys._(api_key_id).get()
print response.response_headers
print response.status_code
print response.response_body

# PATCH
data = {
          "name": "A New Hope"
        }
response = client.api_keys._(api_key_id).patch(request_body=data)
print response.response_headers
print response.status_code
print response.response_body

# PUT
data = {
          "name": "A New Hope",
          "scopes": [
            "user.profile.read",
            "user.profile.update"
          ]
        }
response = client.api_keys._(api_key_id).put(request_body=data)
print response.response_headers
print response.status_code
print response.response_body

# DELETE
response = client.api_keys._(api_key_id).delete()
print response.response_headers
print response.status_code