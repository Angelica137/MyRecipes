import flask
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String)

    @classmethod
    def set_password(self, password):
        self.password = generate_password_hash(self.password, password)

    @classmethod
    def get_password(self, password):
        return check_password_hash(self.password, password)


class Recipe(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True, unique=True)
    recipe_name = db.Column(db.String(50))
    recipe_description = db.Column(db.String(30), unique=True)
    ingredient = db.Column(db.String(30), unique=True)

    @classmethod
    def set_password(self, password):
        self.password = generate_password_hash(self.password, password)

    @classmethod
    def get_password(self, password):
        return check_password_hash(self.password, password)