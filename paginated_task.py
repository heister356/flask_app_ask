import requests


url = 'http://127.0.0.1:5000/v1/paginated_task'
data = {
    'page': '1', 
    'per_page': '2'  
}
token= '.eJyrViotTi2Kz0xRsjLSUUrNTczMUbJSKssszsgrdUgHcfWS83OVdJTSMouKS-LzEnNT4fJA0aL8nFSwZsNaALZqGUo.brGZoUYwny00Hk-PLon73K5oT9k'
headers = {'Authorization': f'Bearer {token}'}
response = requests.post(url, json=data, headers=headers)
if response.status_code == 200:
    print("task paginated successfully!")
    print("Response:", response.text)
else:
    print("Failed to paginate task.")
    print("Response:", response.text)