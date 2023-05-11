from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todos.db"
    app.config["SECRET_KEY"] = os.urandom(24)

    db.init_app(app)

    from .routes import routes
    routes = app.register_blueprint(routes)

    return app