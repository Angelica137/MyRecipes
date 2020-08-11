from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User, Recipe


class SignUpForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('It seems you already have an account. Please log in.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe name', validators=[DataRequired()])
    description = TextAreaField('Decription')
    cook_time = IntegerField('Cooking time')
    servings = IntegerField('Number of servings')
    start_day_before = BooleanField('Start the day before serving')
    lunchbox = BooleanField('Lunchbox safe')
    submit = SubmitField('Add recipe')

    