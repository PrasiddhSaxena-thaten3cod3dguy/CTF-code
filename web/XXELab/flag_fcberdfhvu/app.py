from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "The game is still on."

@app.route("/contents")
def contents():
	return "Hello World!"

@app.route("/contents/flag")
def flag():
	return "HACKERSHALA{xxe_t0_p0rt_scann1ng_t0_fuzz1ng_lyk_4_pr0}"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=1337)