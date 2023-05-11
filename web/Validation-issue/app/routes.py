import jwt
import hashlib
from os import getenv
from flask import Blueprint, flash, make_response, redirect, render_template, request, url_for
from .db import add_user, query_all, query_user

routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    return render_template("index.html")

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
        user_query = query_user(username)
        if len(user_query) != 0:
            flash("User already exists.")
            return redirect(url_for("routes.signup"))
        else:
            password = request.form["password"]
            add_user(username, password)
            flash("User added successfully.")
            return redirect(url_for("routes.signup"))
    else:
        flash("Invalid parameters.")
        return redirect(url_for("routes.signup"))

@routes.route("/login", methods=["POST"])
def login_post():
    if "username" in request.form.keys() and "password" in request.form.keys():
        username = request.form["username"]
        password = hashlib.sha256(request.form["password"].encode()).digest().hex()
        user_query = query_all(username)
        if len(user_query) == 0 or user_query[0][1] != password:
            flash("Invalid credentials.")
            return redirect(url_for("routes.login"))
        else:
            if username.startswith(" "):
                flash("Hacker detected!")
                return redirect(url_for("routes.login"))
            key = getenv("JWT_SECRET")
            payload = {
                "user": username.strip()
            }
            token = jwt.encode(payload, key=key)
            resp = make_response(redirect(url_for("routes.home")))
            resp.set_cookie("auth", token)
            return resp
    else:
        flash("Invalid parameters.")
        return redirect(url_for("routes.login"))

@routes.route("/logout")
def logout():
    if "auth" in request.cookies.keys():
        resp = make_response(redirect(url_for("routes.home")))
        resp.set_cookie("auth", "", expires=0)
        return resp
    else:
        flash("Please login first.")
        return redirect(url_for("routes.login"))

@routes.route("/admin")
def admin():
    if "auth" in request.cookies.keys():
        try:
            key = getenv("JWT_SECRET")
            token = request.cookies["auth"]
            payload = jwt.decode(token, key=key, algorithms=["HS256",])
            print(payload)
            if payload["user"] == "admin":
                return render_template("admin.html")
            else:
                flash("Not Authorized.")
                return redirect(url_for("routes.login"))
        except:
            flash("Tampering detected.")
            return redirect(url_for("routes.login"))
    else:
        flash("Please login as admin.")
        return redirect(url_for("routes.login"))