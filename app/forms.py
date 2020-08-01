from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Optional, Email, Length, EqualTo, ValidationError, email_validator


class LoginForm(FlaskForm):
    email = StringField("Email", [DataRequired(), Email()])
    password = StringField("Password", [DataRequired(), Length(min=6,max=15)])
    submit = SubmitField("Login")


class SignUp(FlaskForm):
    name = StringField("Name", [DataRequired()])
    email = StringField("Email", [DataRequired(), Email()])
    password = StringField("Password", [DataRequired(), Length(min=6, max=15)])
    confirm_password = StringField("Confirm password", [DataRequired(), Length(min=6, max=15), EqualTo("password")])
    submit = SubmitField("Sign up")

    def validate_email(self, email):
        """
        verify email not in use already
        """
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use.")


class RecipeCreate(FlaskForm):
    recipe_name = StringField("Recipe name", [DataRequired()])
    recipe_description = TextAreaField("Description", [Optional()])
    servings = IntegerField("Servings", [DataRequired()])
    submit = SubmitField("Save")

# "add" button for ingredients and cooking steps to
# reveal a new input field
