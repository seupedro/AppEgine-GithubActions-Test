import os
from flask import Flask
app = Flask(__name__)


@app.route("/ping")
def ping():
    return "pong"


@app.route("/")
def root():
    return "Flask App Engine"


@app.route("/env")
def env():
    return os.environ