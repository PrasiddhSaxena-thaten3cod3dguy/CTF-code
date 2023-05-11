from flask import Blueprint, make_response, redirect, render_template, request, send_file, url_for
from db import add_user, query, query_secure
import jwt

routes = Blueprint("routes", __name__)
JWT_KEY = "GujjuTheIncidentResponder31337"

@routes.route("/")
def index():
    if "auth" in request.cookies.keys():
        try:
            token = request.cookies["auth"]
            payload = jwt.decode(token, key=JWT_KEY, algorithms=["HS256",])
            user_data = query(payload["username"])
            if user_data[0][0] == "admin":
                return render_template("index.html")
            return redirect(url_for("routes.logout"))
        except:
            return redirect(url_for("routes.logout"))
    return redirect(url_for("routes.login"))

@routes.route("/login")
def login():
    return render_template("login.html")

@routes.route("/signup")
def signup():
    return render_template("signup.html")

@routes.route("/login", methods=["POST"])
def login_post():
    if "username" in request.form.keys() and "password" in request.form.keys():
        username = request.form["username"]
        password = request.form["password"]
        user_data = query_secure(username)
        if len(user_data) == 0 or user_data[0][1] != password:
            return redirect(url_for("routes.login"))
        payload = {"username": user_data[0][0]}
        token = jwt.encode(payload, key=JWT_KEY)
        resp = make_response(redirect(url_for("routes.index")))
        resp.set_cookie("auth", token)
        return resp
    return redirect(url_for("routes.login"))

@routes.route("/signup", methods=["POST"])
def signup_post():
    if "username" in request.form.keys() and "password" in request.form.keys():
        username = request.form["username"]
        password = request.form["password"]
        user_data = query_secure(username)
        if len(user_data) != 0:
            return redirect(url_for("routes.signup"))
        add_user(username, password)
        return redirect(url_for("routes.login"))
    return redirect(url_for("routes.signup"))

@routes.route("/logout")
def logout():
    if "auth" in request.cookies.keys():
        resp = make_response(redirect(url_for("routes.login")))
        resp.set_cookie("auth", "", 0)
        return resp
    return redirect(url_for("routes.login"))

@routes.route("/downloadfile_88efbc")
def secret_file():
    return send_file("./static/files/Hackershala.wav")

@routes.route("/Hackershalasql887")
def get_flag():
    return "HACKERSHALACTF{34$y_y37_d1ff1cult_ahfhhgs54}"