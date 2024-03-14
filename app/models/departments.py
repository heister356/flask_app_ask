from sqlalchemy import ForeignKey
from datetime import datetime

from app import db
class Departments(db.Model):
    dept_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dept_name = db.Column(db.String, nullable=False, unique=True)
    job_title = db.Column(db.String, nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    created_by = db.Column(db.String, nullable=False)
    emp_id = db.Column(db.Integer, ForeignKey('employees.emp_id')) 
    
    
    #