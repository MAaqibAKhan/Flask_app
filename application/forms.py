from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users
from flask_login import current_user

class PostForm(FlaskForm):
	title = StringField('Title',
		validators=[
			DataRequired(),
			Length(min=1, max=250)
		])
	content = StringField('Post',
		validators=[
			DataRequired(),
			Length(min=10, max=25000)
		])
	submit = SubmitField('Submit Post')

class RegistrationForm(FlaskForm):
	first_name = StringField('First Name',
		validators=[
			DataRequired(),
			Length(min=3, max=30)
		])
	last_name = StringField('Surname',
		validators=[
			DataRequired(),
			Length(min=4, max=30)
		])
	email = StringField('Email address	',
		validators=[	
			DataRequired(),
			Email()
		])
	password = PasswordField('Password 	',
		validators=[
			DataRequired(),
			Length(min=4)
		])
	confirm_password = PasswordField('Confirm Password 	',
		validators=[
			DataRequired(),
			EqualTo('password')
		])
	submit = SubmitField('Register')
	
	def validate_email(self, email):
		user = Users.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email already in use!')

class LoginForm(FlaskForm):
	email = StringField('Email address	',
		validators=[	
			DataRequired(),
			Email()
		])
	password = PasswordField('Password 	',
		validators=[
			DataRequired(),
		])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

	def validate_password(self, email):
		user = Users.query.filter_by(email=email.data).first()
		if user:
			if not bcrypt.check_password_hash(user.password, self.password.data):
				raise ValidationError('Incorrect password!')

class UpdateAccountForm(FlaskForm):
	first_name = StringField('First Name',
		validators=[
			DataRequired(),
			Length(min=3, max=30)
		])
	last_name = StringField('Surname',
		validators=[
			DataRequired(),
			Length(min=4, max=30)
		])
	email = StringField('Email address	',
		validators=[	
			DataRequired(),
			Email()
		])
	submit = SubmitField('Update')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = Users.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Email already in use - Please choose another!')
