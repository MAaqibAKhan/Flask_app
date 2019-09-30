from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(id):
	return Admin.query.get(int(id))

class Admin(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(10), nullable=False, unique=True)
	password = db.Column(db.String(30), nullable=False)

	posts = db.relationship('Logs', backref='author', lazy=True)

	def __repr__(self):
		return ''.join(['Admin ID; ', str(self.id), '\r\n', 'username: ', self.username])

class Continant(db.Model):
	continantID = db.Column(db.String(5), primary_key=True)
	continantName = dbColumn(db.String(50), nullable=False, unique=True)

	def __repr__(self):
		return ''.join([
			'ContinantID: ', self.continantID, '\r\n',
			'Name: ', self.continantName
			])

class Country(db.Model):
	countryID = db.Column(db.String(5), primary_key=True)
	countryName = db.Column(db.String(50), nullable=False, unique=True)
	capital = db.Column(db.String(50), nullable=False)

	continantID = db.Column(db.String(5), db.ForeignKey('Continant.continantID'), nullable=False)

	def __repr__(self):
		return ''.join([
			'CountryID: ', self.countryID, '\r\n',
			'Country: ', self.countryName, '\r\n', 
			'Capital: ', self.capital
			])

#countryList =  Country.query.join(Continant, continantID==Country.continantID).add_columns(Country.countryID, Country.countryName, Country.capital, Country.continantID, Continant.continantID, Continant.continantName)