# from email.mime import application
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from os import path
# from flask_login import LoginManager

# db = SQLAlchemy()
# DB_NAME = "database.db"


def create_app():
    application = Flask(__name__)
    application.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    # application.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # db.init_application(application)

    from .views import views
    from .auth import auth

    application.register_blueprint(views, url_prefix='/')
    application.register_blueprint(auth, url_prefix='/')

    # from .models import User

    # create_database(application)

    # login_manager = LoginManager()
    # login_manager.login_view = 'auth.login'
    # login_manager.init_application(application)

    # @login_manager.user_loader
    # def load_user(id):
    #     return User.query.get(int(id))

    return application


# def create_database(application):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(application=application)
#         print('Created Database!')