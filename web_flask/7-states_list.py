#!/usr/bin/python3
""" A basic flask app it should display the list of Cities in States"""
from flask import Flask
from flask import render_template
from models import storage
from models import state
app = Flask(__name__)


@app.teardown_appcontext
def tear(r):
    storage.close()

@app.route("/states_list")
def LSTC(n):
    """a function that returns a number"""
    dic = storage.all(state)
    lista = list(dic.values)
    lista.sort()
    render_template("7-states_list.py", lista)

