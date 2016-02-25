import os
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from client import Client
    from config import Config


Config()
request_headers = {'X-Mock': 200, 'Content-Type': 'application/json'}
client = Client(host=os.environ.get('MOCK_HOST'),
                api_key=os.environ.get('SENDGRID_API_KEY'),
                request_headers=request_headers,
                version=3)

request_headers = {'X-Mock': 200}
response = client.version(3).api_keys.get()
print response.response_headers
print response.status_code
print response.response_body

request_headers = {'X-Mock': 200}
query_params = {'limit': 100}
response = client.api_keys.get(query_params=query_params,
                               request_headers=request_headers)
print "\nGET Mocked Example"
print response.response_headers
print response.status_code
print response.response_body

data = {'sample': 'data'}
request_headers = {'X-Mock': 201}
response = client.api_keys.post(request_body=data,
                                request_headers=request_headers)
print "\nPOST Mocked Example"
print response.response_headers
print response.status_code
print response.response_body

data = {'sample': 'data'}
request_headers = {'X-Mock': 200}
api_key_id = "test_url_param"
response = client.api_keys._(api_key_id).put(request_body=data,
                                             request_headers=request_headers)
print "\nPUT Mocked Example"
print response.response_headers
print response.status_code
print response.response_body

data = {'sample': 'data'}
request_headers = {'X-Mock': 200}
api_key_id = "test_url_param"
response = client.api_keys._(api_key_id).patch(request_body=data,
                                               request_headers=request_headers)
print "\nPATCH Mocked Example"
print response.response_headers
print response.status_code
print response.response_body

request_headers = {'X-Mock': 204}
api_key_id = "test_url_param"
response = client.api_keys._(api_key_id).delete(
                                          request_headers=request_headers)
print "\nDELETE Mocked Example"
print response.response_headers
print response.status_code
print response.response_body
