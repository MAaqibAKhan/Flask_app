from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError
from application.models import Admin, Continant, Country
from flask_login import current_user

class CountryForm(FlaskForm):
	Country_name = StringField('Country Name',
		validators=[
			DataRequired(),
			Length(max=50)
		])
	capital = StringField('Capital',
		validators=[
			DataRequired(),
			Length(max=50)
		])
	continant = StringField('Continent',
		validators=[
			DataRequired(),
			Length(max=50)
		])
		submit = SubmitField('Update')
	

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

	def validate_email(self, username):
		user != Users.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Incorrect Username')

	def validate_password(self, username):
		admin = Admins.query.filter_by(email=email.data).first()
		if admin:
			if not bcrypt.check_password_hash(user.password, self.password.data):
				raise ValidationError('Incorrect password!')

class CountrySubmitForm(FlaskForm):
	choice = StringField('Country',
		validators=[
			DataRequired()
		])
	submit = SubmitField('Submit')

class CapitalSubmitForm(FlaskForm):
	choice = StringField('Capital City',
		validators=[
			DataRequired()
		])
	submit = SubmitField('Submit')

class CountryUpdateForm(FlaskForm):
	choices[('country','country')
			('capital', 'capital')
			('continant', 'continant')]
	select = SelectField('Search: ', choices=choices)
	search = StringField('')