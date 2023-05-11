from email.mime import base
from flask import Blueprint, make_response, redirect, render_template, request, url_for
import pickle
import base64

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    if "email" in request.cookies.keys():
        try:
            serialized = request.cookies["email"]
            deserialised = pickle.loads(base64.b64decode(serialized))
            if "email" in deserialised.keys():
                return render_template("index.html", email=deserialised["email"])
        except:
            return render_template("index.html")
    return render_template("index.html")

@routes.route("/email", methods=["POST"])
def email():
    if "email" in request.form.keys():
        email = request.form["email"]
        serialized = base64.b64encode(pickle.dumps({"email": email})).decode()
        resp = make_response(redirect(url_for("routes.index")))
        resp.set_cookie("email", serialized)
        return resp
    return redirect(url_for("routes.index"))