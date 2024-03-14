import requests
url = 'http://127.0.0.1:5000/departments'
data = {
    'dept_name': 'HR',  
    'job_title': 'Manager', 
    'created_by': 'admin'  
}
token= '.eJyrVkrNLYjPTFGyMjTTAbITM3OUrJTyEvMysvNKjc1MTB3SQWJ6yfm5SjpKaZlFxSXxeYm5qRBFKRlAwaL8nFSICbUA660Zlg.VxHseaD1d-n8KpUU3do0f9Q4f5A'
headers = {'Authorization': f'Bearer {token}'}
response = requests.post(url, json=data, headers=headers)
if response.status_code == 200:
    print("Department added successfully!")
    print("Response:", response.text)
else:
    print("Failed to add department.")
    print("Response:", response.text)
