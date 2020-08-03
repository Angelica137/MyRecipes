from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate


csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    application = Flask(__name__)
    application.config.from_object('config.Config')
    db.init_app(application)
    csrf.init_app(application)
    migrate.init_app(application)

    
    with application.app_context():
        from . import routes
        db.create_all()
        return application


