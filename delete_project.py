import requests


url = 'http://127.0.0.1:5000/v1/delete_project/7'
token= '.eJyrViotTi2Kz0xRsjLUUUrNTczMUbJSykpMzk9ySAfx9JLzc5V0lNIyi4pL4vMSc1Nh0kDBovycVIjWWgByNRgN.3lccjoeEVbAXwL6JqccKHLJahas'
headers = {'Authorization': f'Bearer {token}'}
response = requests.delete(url, headers=headers)
if response.status_code == 200:
    print("Project deleted successfully!")
    print("Response:", response.text)
else:
    print("Failed to delete project.")
    print("Response:", response.text)
