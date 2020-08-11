from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import SignUpForm, LoginForm
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='iCook')


@app.route('/home')
@login_required
def home():
    user = {'user_name': 'Angelica'}
    recipes = [
			{
          'recipe': 'Fish Tacos',
          'description': 'Delicious fish tacos from Tijuana',
          'time': 25,
          'calories': 400,
			},
			{			
          'recipe': 'Chicken Katsu Curry',
          'description': 'the best chicken katsu ever',
          'time': 20,
          'calories': 350,
			}
		]
    return render_template('home.html', title='Home', user=user, recipes=recipes)


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Welcome aboard {user.username}')
        return redirect(url_for('home'))
    return render_template('sign_up.html', title='Join', form=form)
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is  None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

