from flask import current_app as application
from flask import render_template, request, json, Response
from app.forms import SignUp, LoginForm, RecipeCreate


@application.route("/")
@application.route("/index")
def index():
    return render_template("home.html")


@application.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    form = SignUp()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if request.form.get("email") == "test@test.com":
            flash("Welcome aboard! 🥘", "success")
            return redirect("/index")
        else:
            flash("Sorry, something went wrong 😿", "danger")
    return render_template("sign_up.html", title="Sign up", form=form) 


@application.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.object(email=email).first()
        if user and password == user.password:
            flash(f"Welcome back {user.name}! 👩‍🍳", "success")
            return redirect("/index")
        else:
            flash("Oops... something is broken", "danger")
    return render_template("login.html", title="Login", form=form) 


@application.route("/create_recipe", methods=["GET", "POST"])
def create_recipe():
    form = RecipeCreate()
    return render_template("create_recipe.html", title="Create new recipe", form=form)


