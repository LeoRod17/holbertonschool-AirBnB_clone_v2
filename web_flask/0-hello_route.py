#!/usr/bin/python3
""" A basic flask app it should display Hello HBNB!"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello():
    """a function that returns the hello in the route"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
