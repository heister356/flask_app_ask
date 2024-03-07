import requests

url = 'http://127.0.0.1:5000/remove_data' 
id = {"id": "6VTI8X6LL0MMPJCC"}
response = requests.delete(url, params=id)
print(response.text)
