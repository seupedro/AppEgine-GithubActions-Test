from flask import Flask
app = Flask(__name__)


@app.route("/ping")
def ping():
    return "pong"


@app.route("/")
def ping():
    return "Flask App Engine"
