import sys
sys.dont_write_bytecode = True

from flask import Flask, make_response, redirect, render_template, render_template_string, request, send_file, url_for
import os
import jwt

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(32)
JWT_SECRET = "secret_key" # Super secure, huh ?!?

def check_ip(request):
    if "X-Forwarded-For" in request.headers.keys():
        if request.headers["X-Forwarded-For"] == "127.0.0.1":
            return True
    return False

def check_jwt(token):
    try:
        payload = jwt.decode(token, key=JWT_SECRET, algorithms=["HS256",])
        if payload["role"] != 0 and payload["role"] % 999999 == 0:
            return 1
    except:
        return 3
    return 2

@app.route("/")
def index():
    return render_template("index.html")
    if check_ip(request):
        return render_template("index.html")
    return "Not Authorized."

@app.route("/", methods=["POST"])
def index_post():
    if "name" in request.form.keys():
        name = request.form["name"]
        token = jwt.encode({"user": name, "role": 1}, key=JWT_SECRET)
        resp = make_response(redirect(url_for("blog")))
        resp.set_cookie("token", token)
        return resp
    return redirect(url_for("index"))

@app.route("/blog")
def blog():
    if "token" in request.cookies.keys():
        res = check_jwt(request.cookies["token"])
        if res == 1:
            return redirect(url_for("admin_e2ad645"))
        elif res == 2:
            return render_template("blog.html")
        elif res == 3:
            return redirect(url_for("index"))
    return redirect(url_for("index"))

@app.route("/admin_e2ad645")
def admin_e2ad645():
    if "token" in request.cookies.keys():
        if check_jwt(request.cookies["token"]) == 1:
            return render_template("admin.html")
    return redirect(url_for("index"))

@app.route("/file_05a054b")
def file_05a054b():
    if "token" in request.cookies.keys():
        if check_jwt(request.cookies["token"]) == 1:
            if "name" in request.args.keys():
                try:
                    filename = "static/images/" + request.args["name"]
                    if filename.startswith("static/images/../../app.py"):
                        return redirect(url_for("admin_e2ad645"))
                    return send_file(filename)
                except:
                    return redirect(url_for("admin_e2ad645"))
    return redirect(url_for("admin_e2ad645"))

@app.route("/dev_d4ae547")
def dev_d4ae547():
    if "test" in request.args.keys():
        template = """{% extends 'base.html' %}
        {% block content %}
            $$test$$
        {% endblock %}
        """.replace("$$test$$", request.args["test"])
        return render_template_string(template)
    return "<!-- This endpoint is still under development. -->"

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].strip().lower() == "debug":
        app.debug = True
    app.run("0.0.0.0", 5000)