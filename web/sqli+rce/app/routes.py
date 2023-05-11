import os
import jwt
from flask import Blueprint, make_response, redirect, render_template, request, url_for
from .db import add_user, query, query_secure

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    if "auth" in request.cookies.keys():
        token = request.cookies["auth"]
        secret = os.getenv("JWT_SECRET")
        payload = jwt.decode(token, key=secret, algorithms=["HS256",])
        user_data = query(payload["username"])
        data = " ".join(x[0] for x in user_data)
        return render_template("index.html", data=data)
    return redirect(url_for("routes.login"))

@routes.route("/admin")
def admin():
    if "auth" in request.cookies.keys():
        token = request.cookies["auth"]
        secret = os.getenv("JWT_SECRET")
        payload = jwt.decode(token, key=secret, algorithms=["HS256",])
        user_data = query(payload["username"])
        if user_data[0][0] != "admin":
            return redirect(url_for("routes.login"))
        return render_template("admin.html")
    return redirect(url_for("routes.login"))

@routes.route("/ping_75b99073859f729598ffd77602970878", methods=["POST"])
def ping():
    if "ip" in request.form.keys():
        ip = request.form["ip"]
        output = os.popen("ping -c 4 " + ip).read().split("\n")
        return render_template("admin.html", output=output)
    return redirect(url_for("routes.admin"))

@routes.route("/login")
def login():
    return render_template("login.html")

@routes.route("/signup")
def signup():
    return render_template("signup.html")

@routes.route("/signup", methods=["POST"])
def signup_post():
    if "username" in request.form.keys() and "password" in request.form.keys():
        username = request.form["username"]
        if username == "admin":
            return redirect(url_for("routes.signup"))
        password = request.form["password"]
        add_user(username, password)
        return redirect(url_for("routes.login"))
    return redirect(url_for("routes.signup"))

@routes.route("/login", methods=["POST"])
def login_post():
    if "username" in request.form.keys() and "password" in request.form.keys():
        username = request.form["username"]
        password = request.form["password"]
        user_data = query_secure(username)
        if len(user_data) == 0 or password != user_data[0][1]:
            return redirect(url_for("routes.login"))
        secret = os.getenv("JWT_SECRET")
        token = jwt.encode({"username": username}, key=secret)
        resp = make_response(redirect(url_for("routes.index")))
        resp.set_cookie("auth", token)
        return resp
    return redirect(url_for("routes.login"))

@routes.route("/logout")
def logout():
    if "auth" in request.cookies.keys():
        resp = make_response(redirect(url_for("routes.login")))
        resp.set_cookie("auth", "", 0)
        return resp
    return redirect(url_for("routes.login"))