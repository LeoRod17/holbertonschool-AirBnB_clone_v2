#!/usr/bin/python3
""" A basic flask app it should display texts"""
from flask import Flask
from flask import render_template
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
    "a funtion that returns C + text"
    newTxt = text.replace("_", " ")
    return f'C {newTxt}'


@app.route("/python/")
@app.route("/python/<text>")
def pythonisCool(text="is cool"):
    "a funtion that returns Python + text or is cool by default"
    newTxt = text.replace("_", " ")
    return f'Python {newTxt}'


@app.route("/number/<int:n>")
def NisNumber(n):
    "a funtion that returns a number"
    return f'{n} is a number'


@app.route("/number_template/<int:n>")
def NisTemplate(n):
    "a funtion that returns a number"
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
