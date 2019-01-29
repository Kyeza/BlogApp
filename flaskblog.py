"""Blog flask app"""

from flask import Flask

APP = Flask("__name__")

@APP.route("/")
@APP.route("/home")
def home():
	"""Home view"""
	return "<h1>Home Page</h1>"

@APP.route("/about")
def about():
	"""About view"""
	return "<h1>About Page</h1>"
	