from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.urandom(24)

    from .routes import routes
    app.register_blueprint(routes)

    return app