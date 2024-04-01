import requests

url = 'http://127.0.0.1:5000/remove_data' 
list_id = {'id': '6VTI8X6LL0MMPJCC'}
response = requests.delete(url, params=list_id)
print(response.text)
