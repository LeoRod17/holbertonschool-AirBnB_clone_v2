#!/usr/bin/python3
""" A basic flask app it should display texts"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello():
    """a function that returns the hello in the route"""
    return "Hello HBNB!"


@app.route("/hbnb")
def HBNB():
    "a funtion that returns HBNB"
    return "HBNB"


@app.route("/c/<text>")
def CisF(text):
    "a funtion that returns HBNB"
    newTxt = text.replace("_", " ")
    return f'C {newTxt}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
