#!/usr/bin/python3
""" A basic flask app it should display the list of Cities in States"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def tear(r):
    storage.close()


@app.route("/", strict_slashes=False)
def Welcome():
    """a function that shows a welcoming message"""
    return "Welcome to AirBnB"


@app.route("/cities_by_states", strict_slashes=False)
def ListaSC():
    """a function that returns a list of States with the cities"""
    dic = storage.all(State)
    return render_template("8-cities_by_states.html", state=dic)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
