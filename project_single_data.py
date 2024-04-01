import requests

url = 'http://127.0.0.1:5000/v1/single_data/3' 
token = '.eJyrViotTi2Kz0xRsjLUUUrNTczMUbJSykpMzk9ySAfx9JLzc5V0lNIyi4pL4vMSc1Nh0kDBovycVIjWWgByNRgN.3lccjoeEVbAXwL6JqccKHLJahas'
headers = {'Authorization': f'Bearer {token}'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("project data retrieved successfully!")
    print("Response:", response.json()) 
else:
    print("Failed to retrieve project data.")
    print("Response:", response.text)
