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


@app.route("/states", strict_slashes=False)
def LSTC():
    """a function that returns a list of States"""
    dic = storage.all(State)
    return render_template("7-states_list.html", state=dic)


@app.route("/states/<id>", strict_slashes=False)
def ListaSC(id):
    """a function that returns a list of States with the cities"""
    St = storage.all(State).values()
    ids = "Not Found"
    for state in St:
        if state.id == id:
            ids = id
            break
    return render_template("9-states.html", state=state, Id=ids)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
