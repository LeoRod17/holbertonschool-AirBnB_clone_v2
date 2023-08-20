#!/usr/bin/python3
""" A basic flask app it should display the list of Cities in States"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def tear(r):
    storage.close()


@app.route("/", strict_slashes=False)
def Welcome():
    """a function that shows a welcoming message"""
    return "Welcome to AirBnB"


@app.route("/hbnb_filters", strict_slashes=False)
def ListaSC(id):
    """a function that returns a list of States with the cities"""
    St = storage.all(State)
    Am = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", state=St, Amen=Am)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
