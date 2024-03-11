import requests

url = 'http://127.0.0.1:5000/fetch_data'
user_id =  {"id": "6VTI8X6LL0MMPJCC"}
response = requests.get(url, params=user_id)
print(response.text)

