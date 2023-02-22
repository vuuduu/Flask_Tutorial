from flask import Blueprint 

# a bunch of url link into views
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sing_up():
    return "<p>Sign-Up</p>"


