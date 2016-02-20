from client import Client
from config import Config
import os
Config.init_environment()
headers = {'X-Test1': 'header1', 'X-Test2': 'header2'}
client = Client(host=os.environ.get('HOST'), 
                api_key=os.environ.get('SENDGRID_API_KEY'), 
                headers=headers
                )
more_headers = {'X-Test3': 'header3'}
params = {'mock': '200'}
response = client.api_keys.get(params=params, headers=more_headers)
print "\nGET Mocked Example"
print response.headers
print response.status_code
print response.body

data = {'sample': 'data'}
params = {'mock': 201}
more_headers = {'X-Test4': 'header4'}
response = client.api_keys.post(data=data, params=params, headers=more_headers)
print "\nPOST Mocked Example"
print response.headers
print response.status_code
print response.body

data = {'sample': 'data'}
params = {'mock': 200}
api_key_id = "test_url_param"
response = client.api_keys._(api_key_id).put(data=data, params=params)
print "\nPUT Mocked Example"
print response.headers
print response.status_code
print response.body

data = {'sample': 'data'}
params = {'mock': 200}
api_key_id = "test_url_param"
response = client.api_keys._(api_key_id).patch(data=data, params=params)
print "\nPATCH Mocked Example"
print response.headers
print response.status_code
print response.body

params = {'mock': 204}
api_key_id = "test_url_param"
response = client.api_keys._(api_key_id).delete(params=params)
print "\nDELETE Mocked Example"
print response.headers
print response.status_code
print response.body