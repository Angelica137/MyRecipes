from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class User(UserMixin, db.Model):
    __tablename__ = 'users'

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


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Colum(db.Integer, primary_key=True)
    name = db.Column(db.String(150), index=True)
    description = db.Column(db.String)
    servings = db.Column(db.Integer)
    cook_time = db.Column(db.Integer)
    #meal = db.Column(db.String(64)) add tags
    #utensils = db.Column(db.String(150))
    #ingredients = db.Column(db.String(150))
    instructions = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Recipe {}>'.format(self.body)