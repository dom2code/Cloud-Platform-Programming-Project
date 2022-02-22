from email.mime import application
from Website import create_app

application = create_app()

if __name__ == '__main__':
    application.run(debug=True)
# from flask import Flask
# from flask import Blueprint


# application = Flask(__name__)

# @application.route('/')
# def home():

