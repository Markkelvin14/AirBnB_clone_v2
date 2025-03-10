#!/usr/bin/python3
''' starts a Flask web application  '''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hnbn():
    return "HBNB"


if __name__ == "__main__":
    app.run()
