import requests
import json


user_data = {
    "first_name": "jagan",
    "last_name": "nath",
    "email": "jn@gmail.com",
    "phone": "+1 7457749676",
    "country_code": "IN",
    "address": "r, Gandhinagar P.O kottayam",
    "designation":"engineer_java",
    "hire_date": "2022-01-20",
    "password": "password321"
    
}

url = 'http://127.0.0.1:5000/v1/signup'

response = requests.post(url, json=user_data)

print(response.text)
    