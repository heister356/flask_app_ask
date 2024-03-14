import requests
import json

employee_data = {
    "first_name": "nandh",
    "last_name": "gopan",
    "email": "nanhknu3645@gmail.com",
    "phone": "+1 95(7)698999",
    "country_code": "IN",
    "address": "Vishnukrupa, Gandhinagar P.O kottayam",
    "hire_date": "2024-01-08",
    "password": "password123"
    
}

url = 'http://127.0.0.1:5000/signup'

response = requests.post(url, json=employee_data)

if response.status_code == 201:
    print("Signup successful!")
    print("Employee ID", response.json()['employee_id'])
else:
    print("Signup failed", response.text)
    
    #