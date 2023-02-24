from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# This is the object of the database
db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    # secure cookies for our website (In production secret key should not be shared)
    app.config['SECRET_KEY'] = 'a;sldkjna;lskdjf;lasv;lkasjdflk;j'
    # My sqlalchemy data is store at the sqlite:/// location, which is in website folder (location of init)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    #initialize database
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # setting up the database table
    from .models import User, Note

    create_database(app)

    # managing all the login
    login_manager = LoginManager()
    login_manager.login_view  = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# check if the database already exist
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')


