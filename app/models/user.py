from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True, nullable=False, index=True)
    phone = db.Column(db.String(20), unique=True)
    country_code = db.Column(db.String(5), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    designation = db.Column(db.String(50), nullable = False)
    hire_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.Boolean, nullable=False, default=True)
    role_id = db.Column(db.Integer, nullable=False, default=3)
    password_hash = db.Column(db.Text, nullable=False)
    projects = db.relationship('Project', backref='User', lazy=True)
    