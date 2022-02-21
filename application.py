# from Website import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello():
    return "Hello muttai bonda"
