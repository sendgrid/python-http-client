import os

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from python_http_client.client import Client


api_key = os.environ.get('SENDGRID_API_KEY')
headers = {
    "Authorization": 'Bearer {0}'.format(api_key),
    "Content-Type": "application/json"
}
client = Client(host='http://localhost:4010',
                request_headers=headers,
                version=3)

response = client.version(3).api_keys.get()
print(response.response_headers)
print(response.status_code)
print(response.response_body)

headers = {
    'X-Mock': 200
}
params = {'limit': 100}
response = client.api_keys.get(query_params=params,
                               request_headers=headers)
print('\nGET Mocked Example')
print(response.response_headers)
print(response.status_code)
print(response.response_body)

data = {'sample': 'data'}
headers = {'X-Mock': 201}
response = client.api_keys.post(request_body=data,
                                request_headers=headers)
print('\nPOST Mocked Example')
print(response.response_headers)
print(response.status_code)
print(response.response_body)

data = {'sample': 'data'}
headers = {'X-Mock': 200}
api_key_id = 'test_url_param'
response = client.api_keys._(api_key_id).put(request_body=data,
                                             request_headers=headers)
print('\nPUT Mocked Example')
print(response.response_headers)
print(response.status_code)
print(response.response_body)

data = {'sample': 'data'}
headers = {'X-Mock': 200}
api_key_id = 'test_url_param'
response = client.api_keys._(api_key_id).patch(request_body=data,
                                               request_headers=headers)
print('\nPATCH Mocked Example')
print(response.response_headers)
print(response.status_code)
print(response.response_body)

headers = {'X-Mock': 204}
api_key_id = 'test_url_param'
response = client.api_keys._(api_key_id).delete(request_headers=headers)
print('\nDELETE Mocked Example')
print(response.response_headers)
print(response.status_code)
print(response.response_body)
