from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




db = SQLAlchemy()
migrate = Migrate()
app=None
def create_app():
    global app
    if app is None:
        app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:nandhu123@localhost:5432/project_db'
    app.config['SECRET_KEY'] = 'jhdbchewbifwefsv948r047503nvkjviboirhfoi0840593745832408e'

    db.init_app(app)
    migrate.init_app(app, db)

    print("abc")
    return app