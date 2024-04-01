import requests


url = 'http://127.0.0.1:5000/v1/delete_task/1'
data = {
    'id' : 1
}
token= '.eJyrViotTi2Kz0xRsjLUUUrNTczMUbJSykpMzk9ySAfx9JLzc5V0lNIyi4pL4vMSc1Nh0kDBovycVIjWWgByNRgN.3lccjoeEVbAXwL6JqccKHLJahas'
headers = {'Authorization': f'Bearer {token}'}
response = requests.delete(url, json=data, headers=headers)
if response.status_code == 200:
    print("task deleted successfully!")
    print("Response:", response.text)
else:
    print("Failed to delete task.")
    print("Response:", response.text)
