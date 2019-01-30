"""Blog flask app"""

from flask import Flask, render_template, url_for

APP = Flask("__name__")

# dummy data
posts = [
	{
		'author': 'Corey Schafer',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'April 20, 2018'
	},
	{
		'author': 'Kyeza Arnold',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'April 21, 2018'
	}
]

@APP.route("/")
@APP.route("/home")
def home():
	"""Home view"""
	return render_template('home.html', posts=posts)

@APP.route("/about")
def about():
	"""About view"""
	return render_template('about.html', posts=posts)
