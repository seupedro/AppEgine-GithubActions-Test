import os
import pprint
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
    env = str(os.environ).replace('environ(', '').replace(')', '')
    return str(pprint.pprint(env)) 


@app.route("/echo")
def echo():
    echo = os.popen('echo app.yaml')
    return str(echo.read())


@app.route("/ls")
def ls():
    echo = os.popen('ls -l')
    return str(echo.read())
