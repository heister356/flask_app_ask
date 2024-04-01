import requests

url = 'http://localhost:5000/v1/add_task_project'

data = {
    "name": "add create",
    "description": "Task Description",
    "created_by": 2,
    "project_id": 6,
    "task_members": [9, 10]
}
token= '.eJyrViotTi2Kz0xRsjLSUUrNTczMUbJSKslILCrNc0gHcfWS83OVdJTSMouKS-LzEnNT4fJA0aL8nFSwZsNaALNuGTQ.QMmXenkss2hCKyNixmL1Z84TuME'
headers = {'Authorization': f'Bearer {token}'}
response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.text)
