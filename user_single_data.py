import requests

url = 'http://localhost:5000/v1/user_datas/4' 
token = '.eJyrViotTi2Kz0xRsjLUUUrNTczMUbJSykpMzk9ySAfx9JLzc5V0lNIyi4pL4vMSc1Nh0kDBovycVIjWWgByNRgN.3lccjoeEVbAXwL6JqccKHLJahas'
headers = {'Authorization': f'Bearer {token}'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("User data retrieved successfully!")
    print("Response:", response.json()) 
else:
    print("Failed to retrieve user data.")
    print("Response:", response.text)
