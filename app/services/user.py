#signup

# Check if the required data fields (email, phone, first_name, country_code, address, hire_date) are provided in the input data dictionary
# Validate the format of the email
# ensure phone is valid format
# Check for any missing keys in the input data
# Query the database to see if an employee with the provided email already exists
# If an employee with the same email exists, return an error indicating that the email is already taken
# Generate a password hash for the provided password using a secure hashing algorithm
# Create New Employee
# Create a new employee object with the provided data
# Add the new employee object to the database session
# Commit the session
# If the signup process is successful 
# return successful employee_id of the newly created employee and its status code


# Login

# Input the Employee ID, email, first name, role ID, designation
# Construct a token_data containing the provided information
# Serialize the token_data dictionary using the URL-safe serializer
# Return the generated token
# Attempt to deserialize the token using the URL-safe serializer
# If successful, return the deserialized token data
# If an exception occurs during deserialization, return None
# User login data containing email and password
# Validate the email format. If it's not in the correct format, return an error response
# Retrieve the employee object from the database based on the provided email
# If an employee is found and the password matches the hashed password stored in the database
# Generate a token for the employee using the generate_token function
# Verify the generated token using the verify_token function
# If verification is successful, return response containing the token, token data, and a success status code
# If either the email doesn't exist or the password doesn't match
# Return a failure message



import re
import os
from datetime import datetime
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeSerializer

from app import db
from app.models.user import User



def extract_token_data(token):
    if not token:
        return None, None, {'error': 'Token is missing'}
    
    try:
        _, token = token.split()
        token_data = verify_token(token)
        role_id = token_data['role_id']
        user_id_from_token = token_data['user_id']
        return role_id, user_id_from_token, None
    except:
        return None, None, {'error': 'Token incorrect'}


auth = URLSafeSerializer(os.environ.get("SECRET_KEY"), "auth")
def generate_token(id, email, first_name, role_id):
    token_data = {'user_id': id, 'email': email, 'first_name': first_name, 'role_id': role_id}
    token = auth.dumps(token_data)
    return token

def verify_token(token):
    try:
        token_data = auth.loads(token)
        return token_data
    except:
        return None

 
def login(data):
    if not data.get('email') or not re.match(r"[^@]+@[^@]+\.[^@]+", data.get('email')):
       return jsonify({'error':'Email must be in correct format'}), 400
    password = data.get('password')
    User_obj = User.query.filter_by(email=data.get('email').lower()).first()
    if User_obj and check_password_hash(User_obj.password_hash, password):
       token = generate_token(User_obj.id, User_obj.email, User_obj.first_name, User_obj.role_id)
       token_data = {'id': User_obj.id, 'email': User_obj.email, 'first_name': User_obj.first_name, 'role_id': User_obj.role_id}
       result = {'token': token, 'token_data': token_data, 'status_code':200}
       return result
    else:
       results =  {'message': 'Login failed with invalid user credentials'}
       return results


def signup(data: dict):
    email = data.get('email')
    if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({'error': 'Email must be in correct format'}), 400
    phone = data.get('phone')
    if not phone:
        return jsonify({'error': 'phone not provided'}), 404
    digits = ''.join(filter(str.isdigit, phone))
    if phone.startswith("+"):
        phone = "+" + digits
    missing_keys = [key for key in ['first_name', 'country_code', 'address', 'hire_date'] if not data.get(key)]
    if missing_keys:
        return jsonify({'error': 'key missing'}), 400
    existing_user = User.query.filter(User.email == email).first()
    if existing_user:
        return {'error': 'email already exists'}
    password_hash = generate_password_hash(data['password'])
    new_user = User(
        first_name=data['first_name'],
        last_name=data.get('last_name'),
        email=request.json.get('email'),
        phone=phone,
        country_code=data['country_code'],
        address=data['address'],
        designation=data['designation'],
        hire_date=datetime.strptime(data['hire_date'], '%Y-%m-%d'),  
        password_hash=password_hash 
    )
    db.session.add(new_user)
    db.session.commit()
    r = {'user_id': new_user.id, 'status_code':200}
    result = dict(r)
    return result




# def edit_user(user_id, data):
#     token = request.headers.get('Authorization')
#     if not token:
#         return jsonify({'error': 'Token is missing'}), 401
    
#     try:
#         _, token = token.split()
#         token_data = verify_token(token)
#         role_id = token_data['role_id']
#         user_id_from_token = token_data['user_id']
#     except:
#         return jsonify({'error': 'Token incorrect'}), 401

#     user = User.query.get(user_id)

#     if role_id == 1 or (role_id != 1 and user_id == user_id_from_token):
#         if not user:
#             return jsonify({'error': 'User not found'}), 404

#         if 'email' in data:
#             new_email = data.get('email')
#             if not new_email or not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
#                 return jsonify({'error': 'Email must be in correct format'}), 400
#             existing_user_with_email = User.query.filter(User.email == new_email).first()
#             if existing_user_with_email and existing_user_with_email.id != user_id:
#                 return jsonify({'error': 'Email already exists'}), 400
#             user.email = new_email
        
#         missing_keys = [key for key in ['first_name', 'country_code', 'address', 'hire_date'] if not data.get(key)]
#         if missing_keys:
#           return jsonify({'error': 'key missing'}), 400

#         if 'phone' in data:
#             new_phone = data.get('phone')
#             existing_user_with_phone = User.query.filter(User.phone == new_phone).first()
#             if existing_user_with_phone and existing_user_with_phone.id != user_id:
#                 return jsonify({'error': 'Phone number already exists'}), 400
#             user.phone = new_phone

#         user.first_name = data.get('first_name', user.first_name)
#         user.last_name = data.get('last_name', user.last_name)
#         user.country_code = data.get('country_code', user.country_code)
#         user.address = data.get('address', user.address)
#         user.designation = data.get('designation', user.designation)
#         user.hire_date = data.get('hire_date', user.hire_date)

#         if 'password' in data:
#             new_password = data.get('password')
#             user.password_hash = generate_password_hash(new_password)

#         db.session.commit()

#         updated_user_data = {
#             'id': user.id,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'email': user.email,
#             'phone': user.phone,
#             'country_code': user.country_code,
#             'address': user.address,
#             'designation': user.designation,
#             'hire_date': user.hire_date
#         }

#         return updated_user_data, 200

#     return jsonify({'error': 'Unauthorized'}), 401





def edit_user(user_id, data):
    token = request.headers.get('Authorization')
    role_id, user_id_from_token, error = extract_token_data(token)

    if error:
        return jsonify(error), 401

    user = User.query.get(user_id)

    if role_id == 1 or (role_id != 1 and user_id == user_id_from_token):
        if not user:
            return jsonify({'error': 'User not found'}), 404

        if 'email' in data:
            new_email = data.get('email')
            if not new_email or not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
                return jsonify({'error': 'Email must be in correct format'}), 400
            existing_user_with_email = User.query.filter(User.email == new_email).first()
            if existing_user_with_email and existing_user_with_email.id != user_id:
                return jsonify({'error': 'Email already exists'}), 400
            user.email = new_email
        
        missing_keys = [key for key in ['first_name', 'country_code', 'address', 'hire_date'] if not data.get(key)]
        if missing_keys:
          return jsonify({'error': 'key missing'}), 400

        if 'phone' in data:
            new_phone = data.get('phone')
            existing_user_with_phone = User.query.filter(User.phone == new_phone).first()
            if existing_user_with_phone and existing_user_with_phone.id != user_id:
                return jsonify({'error': 'Phone number already exists'}), 400
            user.phone = new_phone

        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.country_code = data.get('country_code', user.country_code)
        user.address = data.get('address', user.address)
        user.designation = data.get('designation', user.designation)
        user.hire_date = data.get('hire_date', user.hire_date)

        if 'password' in data:
            new_password = data.get('password')
            user.password_hash = generate_password_hash(new_password)

        db.session.commit()

        updated_user_data = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone': user.phone,
            'country_code': user.country_code,
            'address': user.address,
            'designation': user.designation,
            'hire_date': user.hire_date
        }

        return updated_user_data, 200

    return jsonify({'error': 'Unauthorized'}), 401




def delete_data(id: int):
    token = request.headers.get('Authorization')
    role_id, user_id_from_token, error = extract_token_data(token)

    if error:
        return jsonify(error), 401

    if role_id != 1:
        return jsonify({'message': 'no permission'}), 403
    user = User.query.get(id)
    print(user)
    if user:
        db.session.delete(user) 
        db.session.commit()  
        return {'message': 'user deleted successfully'}, 200
    return {'error': 'id incorrect'}, 401




def get_all_data():
    token = request.headers.get('Authorization')
    role_id, user_id_from_token, error = extract_token_data(token)
    if error:
        return jsonify(error), 401
    if role_id != 1:
        return jsonify({'message': 'No permission'}), 403
    data = User.query.all()
    user_list = []
    for user in data:
        user_dict =  {'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'phone': user.phone,
        'country_code': user.country_code,
        'address': user.address,
        'designation': user.designation,
        'hire_date': user.hire_date
    }
        user_list.append(user_dict)
    return jsonify({'data': user_list}), 200



def paginated_data(data):
    token = request.headers.get('Authorization')
    role_id, user_id_from_token, error = extract_token_data(token)
    
    if error:
        return {'error': error}, 401
    
    if role_id != 1:
        return {'message': 'no permission'}, 403
    
    all_users = User.query.all()
    user_list = []
    for user in all_users:
        user_dict = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone': user.phone,
            'country_code': user.country_code,
            'address': user.address,
            'designation': user.designation,
            'hire_date': user.hire_date
        }
        user_list.append(user_dict)
        
    page = request.json.get('page')
    per_page = request.json.get('per_page')
    
    try:
        page = int(page)
        per_page = int(per_page)
        if page <= 0 or per_page <= 0:
            raise ValueError
    except ValueError:
        return {'error': 'Invalid page or per_page values'}, 400
    
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    paginated_users = user_list[start_index:end_index]
    
    return {
        'page': page,
        'per_page': per_page,
        'data': paginated_users
    }, 200

    
    
    
    
    
    
    
    
    
def user_info(id):  
    token = request.headers.get('Authorization')
    role_id, user_id_from_token, error = extract_token_data(token)
    if error:
        return jsonify(error), 401
    data = User.query.filter_by(id=id).first()  
    if not data:
        return jsonify({'error': 'user not found'}), 404  
    user_dict = {
        'id': data.id,
        'first_name': data.first_name,
        'last_name': data.last_name,
        'address': data.address,
        'status': data.status,
        'hire_date': data.hire_date,
        'designation': data.designation
    }
    return jsonify({'data': user_dict}), 200


