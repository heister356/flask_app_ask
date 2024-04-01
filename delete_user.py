import requests


url = 'http://127.0.0.1:5000/v1/delete/3'
data = {
    'id' : 2
}
token= '.eJyrViotTi2Kz0xRsjLSUUrNTczMUbJSKslILCrNc0gHcfWS83OVdJTSMouKS-LzEnNT4fJA0aL8nFSwZsNaALNuGTQ.QMmXenkss2hCKyNixmL1Z84TuME'
headers = {'Authorization': f'Bearer {token}'}
response = requests.delete(url, json=data, headers=headers)
if response.status_code == 200:
    print("Department deleted successfully!")
    print("Response:", response.text)
else:
    print("Failed to delete user.")
    print("Response:", response.text)
