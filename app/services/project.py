import os
from flask import request, jsonify
from itsdangerous import URLSafeSerializer
from app.models.project import Project, Project_members
from app.services.user import verify_token, extract_token_data
from app import db

auth = URLSafeSerializer(os.environ.get("SECRET_KEY"), "auth")
def create_project(data):
    token = request.headers.get('Authorization')
    role_id, user_id_from_token, error = extract_token_data(token)
    if error:
        return jsonify(error), 401
    
    if role_id == 1:
        data = request.json
        project_name = data.get('name')
        description = data.get('description')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        client = data.get('client')
        created_by = data.get('created_by')
        members = data.get('members', [])

        project = Project(name=project_name, description=description, start_date=start_date, end_date=end_date,
                        client=client, created_by=created_by)

        db.session.add(project)
        db.session.commit()

        for id in members:
            member = Project_members(project_id=project.id, user_id=id, created_by=created_by)
            db.session.add(member)

        db.session.commit()

        return {'message': 'Project created successfully'}, 201
    else:
        return {'message': 'no permission'}, 401
    
    
    
    
def paginated_project(data):
    token = request.headers.get('Authorization')
    role_id, user_id_from_token, error = extract_token_data(token)
    if error:
        return {'error': error}, 401
    
    if role_id != 1:
        return {'message': 'no permission'}, 403
    
    all_projects = Project.query.all()
    project_list = []
    for project in all_projects:
        project_dict = {
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'status': project.status,
            'start_date': project.start_date,
            'end_date': project.end_date
        }
        project_list.append(project_dict)
        
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
    paginated_projects = project_list[start_index:end_index]
    
    return {
        'page': page,
        'per_page': per_page,
        'data': paginated_projects
    }, 200



def single_project_data(id):  
    token = request.headers.get('Authorization')
    role_id, user_id_from_token, error = extract_token_data(token)
    if error:
        return jsonify(error), 401
    
    data = Project.query.filter_by(id=id).first()  
    if not data:
        return jsonify({'error': 'Project not found'}), 404  
    project_dict = {
        'id': data.id,
        'name': data.name,
        'description': data.description,
        'status': data.status,
        'start_date': data.start_date,
        'end_date': data.end_date
    }
    return jsonify({'data': project_dict}), 200




def delete_project_data(id: int):
   token = request.headers.get('Authorization')
   role_id, user_id_from_token, error = extract_token_data(token)
   if error:
    return jsonify(error), 401
    
   if role_id != 1:
    return jsonify({'message': 'no permission'}), 403
   project = Project.query.get(id)

   if project:
    db.session.delete(project) 
    db.session.commit()  
    return {'message': 'project deleted successfully'}, 200
   return {'error': 'id incorrect'}, 401



def edit_project(project_id, data):
    token = request.headers.get('Authorization')
    role_id, user_id_from_token, error = extract_token_data(token)
    if error:
        return jsonify(error), 401
    
    if role_id == 1:
        project = Project.query.get(project_id)
        if not project:
            return jsonify({'error': 'Project not found'}), 404

        project_name = data.get('name')
        description = data.get('description')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        client = data.get('client')
        created_by = data.get('created_by')
        members = data.get('members', [])

        project.name = project_name
        project.description = description
        project.start_date = start_date
        project.end_date = end_date
        project.client = client
        project.created_by = created_by

        Project_members.query.filter_by(project_id=project.id).delete()
        for member_id in members:
            member = Project_members(project_id=project.id, user_id=member_id, created_by=created_by)
            db.session.add(member)

        db.session.commit()

        return {'message': 'Project updated successfully'}, 200
    else:
        return {'message': 'No permission'}, 403

