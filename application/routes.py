from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Admin, Country
from application.forms import CountryForm, LoginForm, CountrySubmitForm, CapitalSubmitForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
	postData = Posts.query.all()
	return render_template('home.html', title='Home', posts=postData)

@app.route('/countryquiz', methods=['GET', 'POST'])
def CountryQuiz():
	form=CountrySubmitForm
	if validate_on_submit():
		QuizData
	return render_template('countryquiz.html', title='Country Quiz')

@app.route('/capitalquiz')
def CapitalQuiz():
	return render_template('capitalquiz.html', title='Capital Quiz')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('update'))
	form = LoginForm()
	if form.validate_on_submit():
		user = Admin.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('update'))
	return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))


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

@app.route('/add', methods=['GET','POST'])
@login_required
def add():
	search = CountryUpdateForm(request.form)
	if request.method == 'Post':
		return search_results(search_results)
	form = CountryForm()
	if form.validate_on_submit():
		countryData = country(
			country=form.country.data,
			capital=form.capital.data,
			)
		continentData = conitnant(
			continant=form.continant.data
			)
		db.session.add(countryData, continentData)
		db.session.commit()

@app.route('/update', methods=['GET','POST'])
@login_required
def search_results(search):
    results = []
    search_string = search.data['search']
 
    if search.data['search'] == '':
        qry = db_session.query(Country)
        results = qry.all()
 
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
		return render_template('update.html', title='Update', form=form)