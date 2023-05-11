from flask import Blueprint, redirect, render_template, request, url_for
import imghdr

routes = Blueprint("routes", __name__)

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    if imghdr.what(None, header) == 'jpeg':
        return True
    return False

def encrypt_name(name):
    key = 0xff
    enc_name = ""
    for i in name:
        enc_name += str(hex(ord(i) ^ key)).replace("0x", "")
    return enc_name

@routes.route("/")
def index():
    return render_template("index.html")

@routes.route("/", methods=["POST"])
def index_post():
    if "file" in request.files.keys():
        if validate_image(request.files["file"].stream):
            enc_filename = encrypt_name(request.files["file"].filename)
            request.files["file"].save(f"app/static/uploads/{enc_filename}")
            return render_template("index.html", output=f"Image uploaded to /static/uploads/{enc_filename}")
        else:
            return render_template("index.html", output="Only JPEGs allowed.")
    return render_template("index.html")