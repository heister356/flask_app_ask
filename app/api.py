import re
from flask import request, jsonify
from flask_login import login_user,current_user, login_required
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeSerializer
from run_server import app
from app.models.employee import Employees
from app.models.departments import Departments
from app import db
import os
from dotenv import load_dotenv
load_dotenv()
os.environ.get("SECRET_KEY")



# @app.route('/signup', methods = ['POST'])
# def signup():
#     return 'hello'
#first check the email entered is existing with an account or not
       #for that we check the email in data with email that filtered from database
       #if the  mail exist the return an error code  400
#else assign each data with new data
#the add the new employee to database and commit the data
#return a success message with the status code 201 and created employee_id

@app.route('/signup', methods = ['POST'])
def signup():
    data = request.json
    if not request.json.get('email') or not re.match(r"[^@]+@[^@]+\.[^@]+", request.json.get('email')):
        return jsonify({'error':'Email must be in correct format'}), 400
    
    
    if  data.get('phone'):
        digits = ""
        for i in data.get('phone'):
            if i.isdigit():
               digits += i     
        if data.get('phone').startswith("+"):
            phone = "+" + digits
    else:
        return jsonify({'error':'phone not provided'}), 404
       


    keys = ['first_name', 'country_code','address', 'hire_date' ]   
    for key in keys:
        if not data.get(key):
            raise KeyError         
    
    existing_employee  = Employees.query.filter(Employees.email == request.json.get('email')).first()
    if existing_employee:
        return jsonify({'error':'email already exist'}), 400
    password_hash = generate_password_hash(data['password'])
    new_employee = Employees(
        first_name=data['first_name'],
        last_name=data.get('last_name'),
        email=request.json.get('email'),
        phone=phone,
        country_code=data['country_code'],
        address=data['address'],
        hire_date=datetime.strptime(data['hire_date'], '%Y-%m-%d'),  
        password_hash=password_hash 
    )
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'message': 'Signup successful', 'employee_id': new_employee.emp_id}), 201




auth = URLSafeSerializer(os.environ.get("SECRET_KEY"), "auth")

def generate_token(emp_id, email, first_name, role_id):
    token_data = {'emp_id': emp_id, 'email': email, 'first_name': first_name, 'role_id': role_id}
    token = auth.dumps(token_data)
    return token

@app.route('/login', methods=['POST'])
def login():
    if not request.json.get('email') or not re.match(r"[^@]+@[^@]+\.[^@]+", request.json.get('email')):
       return jsonify({'error':'Email must be in correct format'}), 400
    password = request.json.get('password')
    emp_obj = Employees.query.filter_by(email=request.json.get('email').lower()).first()
    if emp_obj and check_password_hash(emp_obj.password_hash, password):
       token = generate_token(emp_obj.emp_id, emp_obj.email, emp_obj.first_name, emp_obj.role_id)
       token_data = {'emp_id': emp_obj.emp_id, 'email': emp_obj.email, 'first_name': emp_obj.first_name, 'role_id': emp_obj.role_id}
       return jsonify({'message': 'Login successful', 'token':token, 'employee_data':token_data}), 200
    else:
       return jsonify({'message': 'Login failed'}), 401

# def login():
#     if not request.json.get('email') or not re.match(r"[^@]+@[^@]+\.[^@]+", request.json.get('email')):
#         return jsonify({'error':'Email must be in correct format'}), 400
#     emp_obj = Employees.query.filter_by(email=request.json.get('email').lower()).first()
#     if emp_obj and check_password_hash(emp_obj.password_hash, request.json.get('password', '')):
#        token_payload = {'emp_id': emp_obj.emp_id, 'email': emp_obj.email, 'first_name': emp_obj.first_name,'role_id': emp_obj.role_id}
#        auth_token = auth.dumps(token_payload)
#        return jsonify({'message': 'Login successful', 'auth_token':auth_token, 'employee_data':token_payload}), 200
#     else:
#         return jsonify({'message': 'Login failed'}), 401



@app.route('/departments', methods=['POST'])
def add_department():
    token = request.headers.get('Authorization')
    b, token = token.split()
    
    print(type(token))
    if not token:
        return jsonify({'error': 'Token is missing'}), 401
    try:
        token_data = auth.loads(token)
        role_id = token_data['role_id']
        print(role_id, token_data)
    except:
        return jsonify({'error': 'Token incorrect'}), 401
    if role_id != 1:
        return jsonify({'message': 'no permission'}), 403
    data = request.json 
    if not data.get('dept_name') or not data.get('job_title') or not data.get('created_by'):
        return jsonify({'error': 'Missing data'}), 400
    new_department = Departments(dept_name=data.get('dept_name'), job_title=data.get('job_title'), created_by=data.get('created_by'))
    db.session.add(new_department)
    db.session.commit()

    return jsonify({'message': 'Department added successfully'}), 200
