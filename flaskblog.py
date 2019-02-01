"""Blog flask app"""

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

APP = Flask("__name__")
APP.config['SECRET_KEY'] = '610c7d4cf574d1106403c21937017696'

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
	return render_template('about.html', title='About')

@APP.route("/register", methods=['GET', 'POST'])
def register():
	"""Register view"""
	form = RegistrationForm()

	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))

	return render_template('register.html', title='Register', form=form)

@APP.route("/login", methods=['GET', 'POST'])
def login():
	"""Login view"""
	form = LoginForm()
	
	if form.validate_on_submit():
		if form.email.data == 'k@gmail.com' and form.password.data == '12345678':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')

	return render_template('login.html', title='Login', form=form)
