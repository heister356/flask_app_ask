import requests

url = 'http://127.0.0.1:5000/update_name'
id = 'V59OF92YF627HFY0'
name = 'aby'
params = {"id": id, "name": name} 
response = requests.patch(url, params=params)
print(response.text)
