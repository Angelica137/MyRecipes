import flask
from app import db
frpm werkzeug.security import generate_apssword_hash, check_password_hash


class User(db.Model):
    user_id = db.Column(db.Integer unique=True)
    name = db.Column(db.String max_length=50)
    email = db.Column(db.String max_length=30, unique=True)
    password = db.Column(db.String)

    @classmethod
    def set_password(self, password):
        self.password = generate_password_hash(self.password, password)

    @classmethod
    def get_password(self, password):
        return check_password_hash(self.password, password)


class Recipe(db.Model):
    recipe_id = db.Column(db.Integer unique=True)
    recipe_name = db.Column(db.String max_length=50)
    recipe_description = db.Column(db.String max_length=30, unique=True)
    ingredient = db.Column(db.String max_length=30, unique=True)

    @classmethod
    def set_password(self, password):
        self.password = generate_password_hash(self.password, password)

    @classmethod
    def get_password(self, password):
        return check_password_hash(self.password, password)