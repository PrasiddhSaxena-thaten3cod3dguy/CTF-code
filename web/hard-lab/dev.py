import sys
sys.dont_write_bytecode = True

from flask import Flask, render_template, request
from os import urandom
from db import query
from utils import check_field

app = Flask(__name__)
app.config["SECRET_KEY"] = urandom(32)

@app.route("/")
def index():
    if "username" in request.args.keys() and "password" in request.args.keys():
        username = request.args["username"]
        password = request.args["password"]
        if check_field(username) and check_field(password):
            user_data = query(username)
            if len(user_data) == 0 or password != user_data[0][1]:
                return "Incorrect details - " + " ".join([x[0] for x in user_data])
            return "This is just for testing :)"
        return "Dont hack me sir!"
    return render_template("index2.html")

if __name__ == "__main__":
    app.run("127.0.0.1", 31337)