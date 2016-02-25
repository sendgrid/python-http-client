from client import Client
from config import Config
import os
Config.init_environment()
headers = {'X-Mock': 200, 'Content-Type': 'application/json'}
client = Client(host=os.environ.get('HOST'),
                api_key=os.environ.get('SENDGRID_API_KEY'),
                headers=headers,
                version=3)

headers = {'X-Mock': 200}
params = {'limit': 100}
response = client.version(3).api_keys.get()
print response.headers
print response.status_code
print response.body

headers = {'X-Mock': 200}
params = {'limit': 100}
response = client.api_keys.get(params=params, headers=headers)
print "\nGET Mocked Example"
print response.headers
print response.status_code
print response.body

data = {'sample': 'data'}
headers = {'X-Mock': 201}
response = client.api_keys.post(data=data, headers=headers)
print "\nPOST Mocked Example"
print response.headers
print response.status_code
print response.body

data = {'sample': 'data'}
headers = {'X-Mock': 200}
api_key_id = "test_url_param"
response = client.api_keys._(api_key_id).put(data=data, headers=headers)
print "\nPUT Mocked Example"
print response.headers
print response.status_code
print response.body

data = {'sample': 'data'}
headers = {'X-Mock': 200}
api_key_id = "test_url_param"
response = client.api_keys._(api_key_id).patch(data=data, headers=headers)
print "\nPATCH Mocked Example"
print response.headers
print response.status_code
print response.body

headers = {'X-Mock': 204}
api_key_id = "test_url_param"
response = client.api_keys._(api_key_id).delete(headers=headers)
print "\nDELETE Mocked Example"
print response.headers
print response.status_code
print response.body
