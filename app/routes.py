from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import SignUpForm
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='iCook')


@app.route('/home')
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
    

#@app.route('/login', methods=['GET', 'POST'])
# def login():
    