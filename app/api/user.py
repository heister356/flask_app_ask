from flask import Blueprint, jsonify,request
from app.services.user import login, signup, edit_user, delete_data, get_all_data, paginated_data, user_info
user_bp = Blueprint('users_api', __name__)


@user_bp.route('/test', methods = ['GET'])
def test_endpoint():
    return jsonify({'message': 'Success'})



@user_bp.route('/signup', methods=['POST'])
def user_signup():
    """
    this function is for new user signup
    """
    data = signup(request.json)   
    re = {'data': data, 'message': 'Success'}, 200
    return re




@user_bp.route('/login', methods=['POST'])
def user_login():
    """
    this function is for user login
    """
    data = login(request.json)
    if data.get('status_code') == 200:
        res = jsonify({'data': data, 'message': 'Success'}), 200
        return res
    ress = jsonify({'message': 'failed'}), 400
    return ress



@user_bp.route('/profile/<int:user_id>', methods=['PUT'])
def user_edit(user_id):
    """
    This function is for user profile edit
    """
    data = request.json
    result = edit_user(user_id, data)  
    if result[1] == 200:
        return jsonify({'data': result[0], 'message': 'updated successfully'}), 200
    return jsonify({'message': 'failed'}), 400


@user_bp.route('/delete/<id>', methods=['DELETE'])
def del_data(id):
    
    """
    This function is for deleting user data.
    """
    response, status_code = delete_data(id)
    if status_code == 200:
        return jsonify({'data': response, 'message': 'Success'}), 200
    return jsonify({'message': 'failed'}), 400



@user_bp.route('/get_data', methods=['GET'])
def unpage():
    """
    This function is for retrieving unpaginated department data.
    """
    response, status_code = get_all_data()
    return response, status_code



@user_bp.route('/paginated_user', methods=['POST'])
def pageination():
    """
    This function is for fetching paginated user data.
    """
    response, status_code = paginated_data(request.json)
    
    if status_code == 200:
        return jsonify({'data': response, 'message': 'Success'}), status_code
    return jsonify({'message': 'failed'}), status_code




@user_bp.route('/user_datas/<int:id>', methods=['GET']) 
def single_user(id): 
    """
    This function is for retrieving single user data.
    """
    response, status_code = user_info(id)  
    return response, status_code
