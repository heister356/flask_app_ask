import requests

url = 'http://127.0.0.1:5000/add_data'
new_data = {
        "name": "renju",
        "language": "English, Hindi",
        "id": "VBLI24E",
        "bio": "good hardworking man.",
        "version": 6.29
    } 
response = requests.post(url, json=new_data)
print(response.text)
