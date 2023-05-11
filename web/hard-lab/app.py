import sys
sys.dont_write_bytecode = True

from flask import Flask
from os import urandom
from routes import routes
from db import setup

app = Flask(__name__)
app.config["SECRET_KEY"] = urandom(32)
app.register_blueprint(routes)

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].lower() == "debug":
        app.debug = True
    setup()
    app.run("0.0.0.0", 1337)