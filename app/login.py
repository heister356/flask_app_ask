import requests

url = 'http://127.0.0.1:5000/login'
data = {'email': 'nanhknu3645@gmail.com', 'password': 'password123'}  
response = requests.post(url, json=data)

if response.status_code == 200:
    print("login successful!", response.text)
else:
    print("Login failed", response.text)
