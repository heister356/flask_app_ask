from flask import Blueprint, request, jsonify
tasks_bp = Blueprint('tasks', __name__)
from app.services.task import create_task, edit_task, paginated_task, detailed_task,delete_task_data

@tasks_bp.route('/add_task_project', methods=['POST'])
def add_tasks():
    """
    This function is for creating tasks in new project.
    """
    response, status_code = create_task(request.json)
    
    if status_code == 201:
        return jsonify({'data': response, 'message': 'Success'}), status_code
    else:
        return jsonify({'message': 'Failed', 'error': response}), status_code
    
    
    
    
@tasks_bp.route('/edit_task/<int:task_id>', methods=['PUT'])
def edit_task_route(task_id):
    """
    This function is for editing a task.
    """
    response = edit_task(task_id, request.json)
    
    if 'error' in response:
        return jsonify({'message': 'Failed', 'error': response['error']}), 404
    else:
        return jsonify({'data': response, 'message': 'Success'}), 200



@tasks_bp.route('/paginated_task', methods=['POST'])
def pagination_task():
    """
    This function is for fetching paginated project data.
    """
    response, status_code = paginated_task(request.json)
    
    if status_code == 200:
        return jsonify({'data': response, 'message': 'Success'}), status_code
    return jsonify({'message': 'failed'}), status_code



@tasks_bp.route('/single_task_data/<id>', methods=['GET']) 
def single_task(id): 
    """
    This function is for retrieving single project data.
    """
    response, status_code = detailed_task(id)  
    return response, status_code



@tasks_bp.route('/delete_task/<id>', methods=['DELETE'])
def del_data(id):
    
    """
    This function is for deleting task data.
    """
    response, status_code = delete_task_data(id)
    if status_code == 200:
        return jsonify({'data': response, 'message': 'Success'}), 200
    return jsonify({'message': 'failed'}), 400


