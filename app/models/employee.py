from flask import jsonify
from datetime import datetime
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user
from run_server import app
from app import db




class Employees(db.Model):
    emp_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_nam = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True, nullable=False, index=True)
    phone = db.Column(db.String(20), unique=True)
    country_code = db.Column(db.String(5), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    hire_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    status = db.Column(db.Boolean, nullable=False, default=True)
    role_id = db.Column(db.Integer, nullable=False, default=3)
    password_hash = db.Column(db.String(200), nullable=False)
    