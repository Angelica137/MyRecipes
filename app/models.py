import re
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5


def slugify(s):
    return re.sub('[^\w]+', '-', s).lower()


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
        return own_recipes.order_by(Recipe.name.asc())
				

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Recipe(db.Model):
    __tablename__ = 'recipe'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), index=True)
    slug = db.Column(db.String(100), unique=True)
    description = db.Column(db.String)
    servings = db.Column(db.Integer)
    cook_time = db.Column(db.Integer)
    # tags = List
    # utensils = db.Column(db.String(150))
		# picture = image
    # ingredients = list
    # instructions = List
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, *args, **kwargs):
        super(Recipe, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        self.slug = ''
        if self.name:
            self.slug = slugify(self.name)

    def __repr__(self):
        return '<Recipe: %s>' % self.title


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # food = Food
    # quantity = Quantity
    # prep = Prep


class Quantity(db.Model):
    __tablename__ = 'quantity'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)
    quantity_type_id = db.Column(db.Integer, db.ForeignKey('quantity_type.id'))
    #quantity_type = db.relationship('QuantityType', foreign_keys=[quantity_type_id])
    #quantity_type = db.relationship('QuantityType', backref=db.backref('quantity', lazy='dynamic'))
    def __repr__(self):
        return '<Quantity {}>'.format(self.quantity_type)


class QuantityType(db.Model):
    __tablename__ = 'quantity_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    quantity = db.relationship('Quantity', backref='quantity', lazy='dynamic')

    def __repr__(self):
        return '<QuantityType {}>'.format(self.name)


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), index=True, unique=True)
    slug = db.Column(db.String(100), unique=True)
    #macro = List
    #micro = List
    #picture = image

    def __init__(self, *args, **kwargs):
        super(Food, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return '<Food: %s>' % self.name



# class MicroNutrition
# class MicroNutriotionType
# class MacroNutrition
# class MacroNutritionType