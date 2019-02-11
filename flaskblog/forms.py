from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flaskblog.models import User


class RegistrationForm(FlaskForm):
	"""docstring for RegistrationForm"""
	username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
	confirm_password = PasswordField('Confirm Password', 
		validators=[DataRequired(), Length(min=8), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError(f'User already exists with {username.data}')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError(f'User already exists with {email.data}')

	
class LoginForm(FlaskForm):
	"""docstring for LoginForm"""
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
	"""docstring for UpdateAccountForm"""
	username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Update')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError(f'User already exists with {username.data}')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError(f'User already exists with {email.data}')
		

class PostForm(FlaskForm):
	"""docstring for PostForm"""
	title = StringField('Title', validators=[DataRequired()])
	content = TextAreaField('Content', validators=[DataRequired()])
	submit = SubmitField('Post')
		