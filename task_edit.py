import requests

url = 'http://localhost:5000/v1/edit_task/1' 

data = {
    "name": "New Task Names",
    "description": "Updated Task Description",
    "status": True,
    "task_members": [4, 7, 10] 
}

token= '.eJyrViotTi2Kz0xRsjLSUUrNTczMUbJSKslILCrNc0gHcfWS83OVdJTSMouKS-LzEnNT4fJA0aL8nFSwZsNaALNuGTQ.QMmXenkss2hCKyNixmL1Z84TuME'
headers = {'Authorization': f'Bearer {token}'}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.text)
