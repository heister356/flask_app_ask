from flask import Blueprint, jsonify,request
project_bp = Blueprint('userss_api', __name__)
from app.services.project import create_project, paginated_project, single_project_data, delete_project_data, edit_project

@project_bp.route('/project', methods=['POST'])
def create_projects():
    """
    This function is for creating a new project along with project members.
    """
    response, status_code = create_project(request.json)
    
    if status_code == 201:
        return jsonify({'data': response, 'message': 'Success'}), status_code
    return jsonify({'message': 'failed'}), status_code



@project_bp.route('/paginated_project', methods=['POST'])
def pagination():
    """
    This function is for fetching paginated project data.
    """
    response, status_code = paginated_project(request.json)
    
    if status_code == 200:
        return jsonify({'data': response, 'message': 'Success'}), status_code
    return jsonify({'message': 'failed'}), status_code


@project_bp.route('/single_data/<id>', methods=['GET']) 
def single(id): 
    """
    This function is for retrieving single project data.
    """
    response, status_code = single_project_data(id)  
    return response, status_code




@project_bp.route('/delete_project/<int:id>', methods=['DELETE'])
def del_project_data(id):
    
    """
    This function is for deleting user data.
    """
    response, status_code = delete_project_data(id)
    if status_code == 200:
        return jsonify({'data': response, 'message': 'Success'}), 200
    return jsonify({'message': 'failed'}), 400


@project_bp.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """
    Route for updating a project.
    """
    data = request.json
    response, status_code = edit_project(project_id, data)
    return jsonify(response), status_code