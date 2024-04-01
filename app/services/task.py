import os
from flask import request, jsonify
from itsdangerous import URLSafeSerializer
from app.models.task import Task, Task_members
from app.models.user import User
from app.models.project import Project
from app.services.user import verify_token, extract_token_data
from app import db

auth = URLSafeSerializer(os.environ.get("SECRET_KEY"), "auth")

def create_task(data):
    token = request.headers.get('Authorization')
    role_id, user_id_from_token, error = extract_token_data(token)
    if error:
        return jsonify(error), 401
    
    if role_id == 1:
        data = request.json
        name = data.get('name')
        status = data.get('status', True)
        description = data.get('description')
        created_by = data.get('created_by')
        project_id = data.get('project_id')
        task_members = data.get('task_members', [])
        project = Project.query.get(project_id)
        if not project:
            return {'error': 'Project not found'}, 404
        new_task = Task(
            name=name,
            status=status,
            description=description,
            created_by=created_by,
            project_id=project_id
        )
        db.session.add(new_task)
        db.session.commit()
        
        for member_id in task_members:
            member = User.query.get(member_id)
            if member:
                new_task_member = Task_members(
                    created_by=created_by,
                    task_id=new_task.id,
                    user_id=member_id
                )
                db.session.add(new_task_member)
            else:
                db.session.rollback()  
                return {'error': f'User with ID {member_id} not found'}, 404
        
        db.session.commit() 
        
        return {'message': 'Task created successfully'}, 201
    else:
        return {'message': 'No permission'}, 403


def edit_task(task_id, data):
    token = request.headers.get('Authorization')
    role_id, user_id_from_token, error = extract_token_data(token)
    if error:
        return jsonify(error), 401
    
    if role_id == 1:
        task = Task.query.get(task_id)
        if not task:
            return {'error': 'Task not found'}, 404
        
        name = data.get('name')
        status = data.get('status')
        description = data.get('description')
        task_members = data.get('task_members', [])
        if name != task.name and Task.query.filter_by(name=name).first():
            return {'error': 'Task name already exists'}, 400
        
        if name:
            task.name = name
        if status is not None:
            task.status = status
        if description:
            task.description = description
        for task_member in task.task_members:
            if task_member.user_id not in task_members:
                db.session.delete(task_member)
        for member_id in task_members:
            member = User.query.get(member_id)
            if member:
                task_member = Task_members.query.filter_by(task_id=task_id, user_id=member_id).first()
                if not task_member:
                    new_task_member = Task_members(
                        created_by=user_id_from_token,
                        task_id=task_id,
                        user_id=member_id
                    )
                    db.session.add(new_task_member)
            else:
                return {'error': f'User with ID {member_id} not found'}, 404
        
        db.session.commit() 
        
        return {'message': 'Task updated successfully'}, 200
    else:
        return {'message': 'No permission'}, 403



 
def paginated_task(data):
    token = request.headers.get('Authorization')
    role_id, user_id_from_token, error = extract_token_data(token)
    if error:
        return {'error': error}, 401
    
    if role_id != 1:
        return {'message': 'No permission'}, 403
    
    all_tasks = Task.query.all()
    task_list = []
    for task in all_tasks:
        task_dict = {
            'id': task.id,
            'name': task.name,
            'description': task.description,
            'status': task.status,
            'created_by': task.created_by,
            'project_id': task.project_id
        }
        task_list.append(task_dict)
    page = data.get('page')
    per_page = data.get('per_page')
    try:
        page = int(page)
        per_page = int(per_page)
        if page <= 0 or per_page <= 0:
            raise ValueError
    except ValueError:
        return {'error': 'Invalid page or per_page values'}, 400
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    paginated_tasks = task_list[start_index:end_index]
    return {
        'page': page,
        'per_page': per_page,
        'data': paginated_tasks
    }, 200



    
def detailed_task(id):
    token = request.headers.get('Authorization')
    role_id, user_id_from_token, error = extract_token_data(token)
    if error:
        return jsonify(error), 401
    
    task = Task.query.filter_by(id=id).first()
    if not task:
        return jsonify({'error': 'Task not found'}), 404  
    
    task_dict = {
        'id': task.id,
        'name': task.name,
        'description': task.description,
        'status': task.status,
        'created_by': task.created_by,
        'project_id': task.project_id
    }
    return jsonify({'data': task_dict}), 200


def delete_task_data(id: int):
    token = request.headers.get('Authorization')
    role_id, user_id_from_token, error = extract_token_data(token)
    if error:
        return jsonify(error), 401
    
    if role_id != 1:
        return jsonify({'message': 'No permission'}), 403
    
    task = Task.query.get(id)

    if task:
        db.session.delete(task)
        db.session.commit()
        return {'message': 'Task deleted successfully'}, 200
    return {'error': 'ID incorrect'}, 404
