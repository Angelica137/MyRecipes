import wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User, Recipe, Tag, Ingredient


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

    
class TagField(wtforms.StringField):
    def _value(self):
        if self.data:
            '''
            Display tags as a comma-separated list
            '''
            return ', '.join([tag.name for tag in self.data])
        return ''

    def get_tags_from_string(self, tag_string):
        raw_tags = tag_string.split(',')
        '''
        Filter out any empty tags
        '''
        tag_names = [name.strip() for name in raw_tags if name.strip()]
        '''
        Query that database and retrieve any tags we have already save
        '''
        existing_tags = Tag.query.filter(Tag.name.in_(tag_names))
        '''
        Determine which tag names are new
        '''
        new_names = set(tag_names) - set([tag.name for tag in existing_tags])
        '''
        Create a  list of unsaved Tag instances for the new tags
        '''
        new_tags = [Tag(name=name) for name in new_names]
        '''
        Return all the existing tags + all the new, unsaved tags
        '''
        return list(existing_tags) + new_tags

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = self.get_tags_from_string(valuelist[0])
        else:
            self.data = []


class RecipeForm(FlaskForm):
    name = StringField('Recipe name', validators=[DataRequired()])
    description = TextAreaField('Decription')
    cook_time = IntegerField('Cooking time')
    servings = IntegerField('Number of servings')
    tags = TagField('Tags', description='Separate multiple tags with commas')
    submit = SubmitField('Add recipe')

    def save_recipe(self, recipe):
        self.populate_obj(recipe)
        recipe.generate_slug()
        return recipe


class FoodForm(FlaskForm):
    name = StringField('Name')

    def get_tags_from_string(self, tag_string):
        '''
        Query the database and retrieve any food we have already saved
        '''
        existing_food = Food.query.filter(Food.name.in_(food_names))
        '''
        Determine which food names are new
        '''
        new_names = set(food_names) - set([food.name for food in existing_foods])
        '''
        Create a  list of unsaved Food instances for the new foods
        '''
        new_foods = [Food(name=name) for name in new_names]
        '''
        Return all the existing foods + all the new, unsaved foods
        '''
        return list(existing_foods) + new_foods

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = self.get_tags_from_string(valuelist[0])
        else:
            self.data = []
