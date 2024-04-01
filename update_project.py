import requests

url = 'http://localhost:5000/v1/projects/3'

data = {
    "name": "Project Name6",
    "description": "Project Description 3456",
    "start_date": "2024-05-28T00:00:00",
    "end_date": "2024-01-28T00:00:00",
    "client": "Client Name1244",
    "created_by": 2, 
    "members": [4, 5, 6] 
}
token= '.eJyrViotTi2Kz0xRsjLSUUrNTczMUbJSKslILCrNc0gHcfWS83OVdJTSMouKS-LzEnNT4fJA0aL8nFSwZsNaALNuGTQ.QMmXenkss2hCKyNixmL1Z84TuME'
headers = {'Authorization': f'Bearer {token}'}
response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.text)