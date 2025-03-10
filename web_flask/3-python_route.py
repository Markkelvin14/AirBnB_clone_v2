#!/usr/bin/python3
''' starts a Flask web application  '''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
        return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text_c(text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text_python(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run()
