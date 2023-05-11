from flask import Blueprint, make_response, redirect, render_template, request, send_file, url_for
from db import query_secure
from utils import check_filename, check_url, get_image
import jwt
import os

routes = Blueprint("routes", __name__)
jwt_secret = "nfeiunbguhjerntgujinerdigvnjmeoikrdmjf3owaeodlk2qoaiwrfnceuirsfgvnrdk"

@routes.route("/")
def index():
    return render_template("index.html")

@routes.route("/", methods=["POST"])
def index_post():
    if "url" in request.form.keys():
        if not check_url(request.form["url"]):
            url = request.form["url"]
            os.popen("rm static/img/*")
            name = "/" + get_image(url)
            return render_template("index.html", name=name)
    return redirect(url_for("routes.index"))

@routes.route("/login")
def login():
    return render_template("login.html")

@routes.route("/login", methods=["POST"])
def login_post():
    if "username" in request.form.keys() and "password" in request.form.keys():
        username = request.form["username"]
        password = request.form["password"]
        user_data = query_secure(username)
        if len(user_data) == 0 or password != user_data[0][1]:
            return redirect(url_for("routes.login"))
        token = jwt.encode({"role": "admin"}, key=jwt_secret)
        resp = make_response(redirect(url_for("routes.admin")))
        resp.set_cookie("auth", token)
        return resp
    return redirect(url_for("routes.login"))

@routes.route("/admin")
def admin():
    if "auth" in request.cookies.keys():
        try:
            payload = jwt.decode(request.cookies["auth"], key=jwt_secret, algorithms=["HS256",])
            if payload["role"] == "admin":
                return render_template("admin.html")
            return redirect(url_for("routes.login"))
        except:
            return redirect(url_for("routes.login"))
    return redirect(url_for("routes.login"))

@routes.route("/getfile_cae27cc9ebb9")
def getfile():
    if "filename" in request.args.keys():
        if not check_filename(request.args["filename"]):
            try:
                return send_file(request.args["filename"])
            except:
                return redirect(url_for("routes.admin"))
    return redirect(url_for("routes.admin"))