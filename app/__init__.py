import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
    db.init_app(app)
    migrate.init_app(app, db)
    from app.api.user import user_bp
    from app.api.project import project_bp
    from app.api.task import tasks_bp
    app.register_blueprint(user_bp, url_prefix='/v1')
    app.register_blueprint(project_bp, url_prefix='/v1')
    app.register_blueprint(tasks_bp, url_prefix='/v1')
    return app
