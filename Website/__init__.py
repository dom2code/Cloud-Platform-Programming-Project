from email.mime import application
from flask import Flask

def create_app():
    application = Flask(__name__)
    application.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

    from .views import views
    from .auth import auth

    application.register_blueprint(views, url_prefix='/')
    application.register_blueprint(auth, url_prefix='/')
    return application

