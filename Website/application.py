from flask import Flask

def create_app():
    application = Flask(__name__)
    application.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

    return application