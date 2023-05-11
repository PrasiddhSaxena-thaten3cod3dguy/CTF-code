import sys
sys.dont_write_bytecode = True

from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(32)

@app.route("/")
def index():
    if "domain" in request.args.keys():
        domain = request.args["domain"]
        blacklist = ["~", "!", "@", "#", "$", "^", " &", "*", "(", ")", "_", "+", "=", "{", "}", "[", "]", '"', ";", ":", "|", "\\", "?", "<", ","]
        for word in blacklist:
            if word in domain:
                return render_template("index.html", output=["Hacker Detected!"])
        output = os.popen("whois " + domain).read().split("\n")
        return render_template("index.html", output=output)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()