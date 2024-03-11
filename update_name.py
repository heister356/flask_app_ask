import requests

url = 'http://127.0.0.1:5000/update_name'
user_id = 'V59OF92YF627HFY0'
name = 'aby'
params = {"id": user_id, "name": name} 
response = requests.patch(url, params=params)
print(response.text)
