import sys
sys.dont_write_bytecode = True

from flask import Flask
from views import routes
from db import setup_db
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(32)
app.register_blueprint(routes)

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].strip().lower() == "debug":
        app.debug = True
    setup_db()
    app.run("0.0.0.0", 1337)