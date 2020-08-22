from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(120))
    recipes = db.relationship('Recipe', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def own_recipes(self):
        own_recipes = Recipe.query.filter_by(user_id=self.id)
        return own_recipes.order_by(Recipe.recipe_name.asc())
				

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(150), index=True)
    description = db.Column(db.String)
    servings = db.Column(db.Integer)
    cook_time = db.Column(db.Integer)
    #tags = List
    #utensils = db.Column(db.String(150))
		#picture = image
    #ingredients = db.Column(db.String(150))
    start_day_before = db.Column(db.Boolean, default=False)
    lunchbox = db.Column(db.Boolean, default=False, index=True)
    # instructions = List
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Recipe {}>'.format(self.body)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(150), index=True, unique=True)
    description = db.Column(db.String)


class Utensil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #food = Food
    #quantity = Quantity
    # prep = Prep


class Quantity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #vlue = float
    #quantity_type = Quantity type


class QuantityType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(150), index=True, unique=True)
    #macro = List
    #micro = List
    #picture = image



# class MicroNutrition
# class MicroNutriotionType
# class MacroNutrition
# class MacroNutritionType