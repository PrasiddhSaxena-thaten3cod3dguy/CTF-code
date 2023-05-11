from flask import Flask
from os import urandom

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] =  urandom(24)

    from .db import setup
    setup()

    from .web import web
    app.register_blueprint(web)

    from .api import api
    app.register_blueprint(api)

    return app