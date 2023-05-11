import sys
sys.dont_write_bytecode = True

from flask import Flask, redirect, render_template, request, url_for
import hashlib
import random
import string
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(32)

def get_sha256(string):
    return hashlib.sha256(string.encode()).hexdigest()

def run_exiftool(filename):
    try:
        dirname = os.path.dirname(os.path.realpath(__file__))
        if "tools" in os.listdir(dirname) and "exiftool" in os.listdir(f"{dirname}/tools"):
            return os.popen(f"{dirname}/tools/exiftool {filename}").read()
    except:
        return "ERROR: In finding tool"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def index_post():
    if "file" in request.files.keys():
        fileobj =  request.files["file"]
        fileobj.seek(0)
        fname = f"/tmp/{''.join([random.choice(string.ascii_letters) for _ in range(10)])}"
        with open(fname, "wb") as wf:
            wf.write(fileobj.read())
        exif_output = run_exiftool(fname).replace('ExifTool Version Number         : 12.23\n', "")
        return render_template("index.html", output=exif_output.split("\n"))
    return redirect(url_for("index"))

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].strip().lower() == "debug":
        app.debug = True
    app.run("0.0.0.0", 5000)