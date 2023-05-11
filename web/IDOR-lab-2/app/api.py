from flask import Blueprint, flash, jsonify, request
from .db import add_user, check_user, query, query_id
import hashlib

api = Blueprint("api", __name__, url_prefix="/api/v1")
api_key = "527e3b6bf06f3d3358905af67c588b1ba621a8599b6010e1a0556632b3c5a2ee"

@api.route("/test")
def test():
    return "All good!"

@api.route("/user/create/<key>", methods=["POST"])
def signup_post(key):
    if key != api_key:
        return jsonify({"error": "Invalid key"})
    else:
        if "username" in request.form.keys() and "password" in request.form.keys():
            username = request.form["username"]
            password = request.form["password"]
            user_exists = check_user(username)
            if len(user_exists) != 0:
                return jsonify({"error": "User already exists."})
            else:
                add_user(username, password)
                return jsonify({"msg": "User successfully added!"})
        else:
            return jsonify({"error": "Invalid parameters."})

@api.route("/user/login/<key>", methods=["POST"])
def login_post(key):
    if key != api_key:
        return jsonify({"error": "Invalid key"})
    else:
        if "username" in request.form.keys() and "password" in request.form.keys():
            username = request.form["username"]
            password = hashlib.sha256(request.form["password"].encode()).digest().hex()
            user_data = query(username)
            if len(user_data) == 0 or password != user_data[0][1]:
                return jsonify({"error": "Incorrect details."})
            else:
                return jsonify({"msg": "ok"})
        else:
            return jsonify({"error": "Invalid parameters."})

@api.route("/users")
def unauthorized_users():
    return jsonify({"error": "Not authorized"})

@api.route("/users/<key>")
def users_without_id(key):
    if key != api_key:
        return jsonify({"error": "Invalid key"})
    return jsonify({"error": "provide user id"})

@api.route("/users/<key>/<id>")
def users(key, id):
    if key != api_key:
        return jsonify({"error": "Invalid key"})
    else:
        user_data = query_id(id)
        if len(user_data) == 0:
            return jsonify({"error": "Could not find user"})
        else:
            return jsonify({"user": user_data[0][0]})

@api.route("/users/<key>/<id>/<text>")
def users_without_flag(key, id, text):
    if key != api_key:
        return jsonify({"error": "Invalid key"})
    else:
        user_data = query_id(id)
        if len(user_data) == 0:
            return jsonify({"error": "Could not find user"})
        else:
            if user_data[0][0] == "admin":
                if text != "flag":
                    return jsonify({"Hello": user_data[0][0], "msg": "Ask for what you want"})
                else:
                    return jsonify({"Hello": user_data[0][0], "msg": "HACKERSHALA{1D0Rs_1n_API_vhnrdfvijg}"})
            else:
                return {"error": "Not Authorized"}