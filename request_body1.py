import requests

url = 'http://127.0.0.1:5000/paginated_data'
values = {'page': '4', 'per_page': 5}  
response = requests.post(url, params=values)
print(response.text)
