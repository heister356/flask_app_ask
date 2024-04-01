import requests

url = 'http://127.0.0.1:5000/v1/login'
data = {'email': 'tharun@gmail.com', 'password': 'password321'}  
response = requests.post(url, json=data)
print(response.text)
