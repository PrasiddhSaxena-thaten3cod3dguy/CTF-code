from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "You can see me ?!?"

@app.route("/flag")
def flag():
    return "HACKERSHALA{p3rf0rm1ng_1nt3rn4l_p0rt_sc4n_thr0ugh_SSRF_chgdrbyturg}"

if __name__ == "__main__":
    app.run("127.0.0.1", port=1337)