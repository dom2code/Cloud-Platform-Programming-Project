from flask import Blueprint, render_template
# from .models import User
# from werkzeug.security import generate_password_hash, check_password_hash
# from . import db
# from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)




@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout<p>"

@auth.route('/signup')
def signup():
    return render_template("sign_up.html")





