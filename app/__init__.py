from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



db = SQLAlchemy()
migrate = Migrate()

from app import models

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://doadmin:aaa@localhost:5432/testdb'
    app.config['SECRET_KEY'] = 'jhdbchewbifwefsv948r047503nvkjviboirhfoi0840593745832408e'

    db.init_app(app)
    migrate.init_app(app, db)
    from app.api import bp as api_bp
    # app.register_blueprint(api_bp, url_prefix='/v1')
    app.register_blueprint(api_bp, url_prefix='/v1')
    print("created app")
    return app
