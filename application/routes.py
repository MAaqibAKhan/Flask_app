from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Admin, Country, Continant
from application.forms import CountryForm, LoginForm, CountrySubmitForm, CapitalSubmitForm, SearchForm, CountryUpdateForm
from flask_login import login_user, current_user, logout_user, login_required

searchTerm = []
newTerm = []

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

@app.route('/countryquiz', methods=['GET', 'POST'])
def countryquiz():
	correctAnswer= False
	answerArray = []
	form=CountrySubmitForm()
	if form.validate_on_submit():
		quizData = Country.query.filter_by(countryName=form.choice.data).first()
		answerArray.append([str(quizData)])
		answerTerm = answerArray[0][0].split(", ")
		answer = answerTerm[1]
		#answerArray = eval("[",str[quizData],"]")
		#answer = answerArray[1]
		print(answer)
		if answer == form.choice.data:
			correctAnswer= True
		if answer != form.choice.data:
			print("False")
	else:
		print(form.errors)
		redirect(url_for('login'))
	return render_template('countryquiz.html', title='Country Quiz', form=form, correctAnswer=correctAnswer)

@app.route('/capital', methods=['GET', 'POST'])
def capital():
	answerArray =[]
	correctAnswer= False
	form=CapitalSubmitForm()
	if form.validate_on_submit():
		quizData = Country.query.filter_by(capital=form.choice.data).first()
		answerArray.append([str(quizData)])
		answerTerm = answerArray[0][0].split(", ")
		answer = answerTerm[2]
		if answer == form.choice.data:
			correctAnswer = True
	return render_template('capital.html', title='Capital Quiz', form=form, correctAnswer=correctAnswer)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('search'))
	form = LoginForm()
	if form.validate_on_submit():
		admin = Admin.query.filter_by(username=form.username.data).first()
		if admin:
			login_user(admin, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('login'))
	return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/add', methods=['GET', 'POST'])
def add():
	form = CountryForm()
	if form.is_submitted():
		countryData = Country(
			countryID = form.countryID.data,
			countryName = form.countryName.data,
			capital = form.capital.data,
			continant_ID = form.continantID.data
			)
		continantData = Continant(
			continantName = form.continant.data
			)
		db.session.add(countryData, continantData)
		db.session.commit()
	return render_template('add.html', title='Add', form=form)

@app.route('/search', methods=['GET','POST'])
@login_required
def search():
	search = SearchForm()
	form = CountryUpdateForm()
	if request.method == 'POST':
		#if search.validate_on_submit():
		searchData = Country.query.filter_by(countryName=search.search.data)
		print(searchData.first())
		print([str(searchData.first())][0][0:5])
		if searchData:
			#for column in searchData:
#			searchTerm = searchData.split(",")
			searchTerm.append([str(searchData.first())]) #Country.countryName.data
			print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSS", searchTerm[0])
			return redirect(url_for('details'))
		else:
			return redirect(url_for('home'))
#	else:
#		searchTerm = ""
#		return redirect(url_for('details'))

	else:
		return render_template('search.html', title='Search', search=search, form=form)

@app.route('/details', methods=['GET','POST'])
@login_required
def details():
	global newTerm
	form = CountryUpdateForm()
	if searchTerm:	
		newTerm = searchTerm[0][0].split(",")
		searchData = Country.query.filter_by(countryName=newTerm[1].strip()).first()
		if form.validate_on_submit():
			if form.delete.data:
				db.session.delete(searchData)
				db.session.commit()
				return redirect(url_for('search'))
			else:
				newTerm[0] = form.countryID.data
				newTerm[1] = form.countryName.data
				newTerm[2] = form.capital.data
				searchData.countryID = form.countryID.data
				searchData.countryName = form.countryName.data
				searchData.capital = form.capital.data
				db.session.commit()
				return redirect (url_for('details'))
		elif request.method =='GET':
			form.countryID.data = searchData.countryID
			form.countryName.data = searchData.countryName
			form.capital.data = searchData.capital
				
		return render_template('details.html', title='Details', form=form)
	return render_template('details.html', title='Details', form=form)


@app.route('/logs', methods=['GET','POST'])
@login_required
def logs():
	form = PostForm()
	if form.validate_on_submit():
		postData = Posts(
			title=form.title.data,
			content=form.content.data,
			author=current_user
			)
		db.session.add(postData)
		db.session.commit()
		return redirect(url_for('home'))
	else:
		print(form.errors)
	return render_template('logs.html', title='Logs', form=form)