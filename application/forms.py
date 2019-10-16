from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError
from application.models import Admin, Continant, Country
from flask_login import current_user
from application import bcrypt, db

class CountrySubmitForm(FlaskForm):
	choice = StringField('Country',
		validators=[
			DataRequired(),
			Length(min=1, max=50)
		])
	submit = SubmitField('Submit')

	def validate_answer(self, choice):
		answer = Country.query.filter_by(countryName=self.choice.data).first()
		if not answer:
			raise ValidationError('Wrong Answer!')

class CapitalSubmitForm(FlaskForm):
	choice = StringField('Capital City',
		validators=[
			DataRequired()
		])
	submit = SubmitField('Submit')

class SearchForm(FlaskForm):
	search = StringField('Search',
		validators=[
			DataRequired(),
			Length(min=1, max=50)
		])
	submit = SubmitField('Search')

class CountryForm(FlaskForm):
	countryID = StringField('Country ID',
		validators=[
			DataRequired(),
			Length(min=5, max=5)
			])
	countryName = StringField('Country Name',
		validators=[
			DataRequired(),
			Length(max=50)
		])
	capital = StringField('Capital',
		validators=[
			DataRequired(),
			Length(max=50)
		])
	continantID = StringField('Continent ID',
		validators=[
			DataRequired(),
			Length(min=5, max=5)
			])
	continant = StringField('Continent',
		validators=[
			DataRequired(),
			Length(max=50)
		])
	submit = SubmitField('Add')
	
class CountryUpdateForm(FlaskForm):
	countryID = StringField('Country ID',
		validators=[
			DataRequired(),
			Length(min=5, max=5)
			])
	countryName = StringField('Country Name',
		validators=[
			DataRequired(),
			Length(max=50)
		])
	capital = StringField('Capital',
		validators=[
			DataRequired(),
			Length(max=50)
		])
	submit = SubmitField('Update')
	delete = SubmitField('Delete')
class LoginForm(FlaskForm):
	username = StringField('Username',
		validators=[	
			DataRequired(),
		])
	password = PasswordField('Password ',
		validators=[
			DataRequired(),
		])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

	def validate_username(self, username):
		user = Admin.query.filter_by(username=self.username.data).first()
		if not user:
			raise ValidationError('Incorrect Username!')

	def validate_password(self, password):
		user = Admin.query.filter_by(username=self.username.data).first()
		if self.password.data != user.password:
			#if not bcrypt.check_password_hash(admin.password, Admin.password.data):
			raise ValidationError('Incorrect password!')