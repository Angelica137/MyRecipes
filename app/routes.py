from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import SignUpForm, LoginForm, RecipeForm
from app.models import User, Recipe
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='iCook')


@app.route('/home')
@login_required
def home():
    recipes = current_user.own_recipes().all()
    return render_template('home.html', title='Home', recipes=recipes)


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
        flash('Welcome aboard {current_user.username}')
        return redirect(url_for('home'))
    return render_template('sign_up.html', title='Join', form=form)


@app.route('/login/', methods=['GET', 'POST'])
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


@app.route('/add_recipe', methods=['GET', 'POST'])
@login_required
def add_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(recipe_name=form.recipe_name.data, description=form.description.data, cook_time=form.cook_time.data, start_day_before=form.start_day_before.data, lunchbox=form.lunchbox.data, author=current_user)
        db.session.add(recipe)
        db.session.commit()
        flash('Your recipe has been saved')
        return redirect(url_for('home'))
    return render_template('add_recipe.html', title='Add your awesome recipe here', form=form)
