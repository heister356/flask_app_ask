import requests

url = 'http://localhost:5000/v1/project'

data = {
    "name": "Project Name10",
    "description": "Project Desc",
    "start_date": "2024-07-28T00:00:00",
    "end_date": "2024-09-28T00:00:00",
    "client": "Client ",
    "created_by": 2, 
    "members": [9, 10, 12] 
}
token= '.eJyrViotTi2Kz0xRsjLSUUrNTczMUbJSKslILCrNc0gHcfWS83OVdJTSMouKS-LzEnNT4fJA0aL8nFSwZsNaALNuGTQ.QMmXenkss2hCKyNixmL1Z84TuME'
headers = {'Authorization': f'Bearer {token}'}
response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.text)
