import requests

url = 'http://127.0.0.1:5000/v1/profile/3'  
data = {
    'first_name': 'saruns',
    'last_name': 'p',
    'email': 'sp@gmail.com',
    'phone': '+1 982943997876',
    'country_code': 'US',
    'address': 'Address12  123',
    'designation': 'network',
    'hire_date': '2022-01-30',
    'password': 'password321'
}
token= '.eJyrViotTi2Kz0xRsjLWUUrNTczMUbJSSsxNzCl1SAfx9JLzc5V0lNIyi4pL4vMSc1Nh0kDBovycVIjWWgB2shgz.mNT2mhb1sSE5po456oYSkcfE5gU'
headers = {'Authorization': f'Bearer {token}'}
response = requests.put(url, json=data, headers=headers)
print(response.text)
