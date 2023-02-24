from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import *
# securing the password
from werkzeug.security import generate_password_hash, check_password_hash
# make logining so much easier
from flask_login import login_user, login_required, logout_user, current_user

# a bunch of url link into views
auth = Blueprint('auth', __name__)

# route is the path address aka url link
# you can create variable inside of render_template where it'll display that variable inside of .html file [var=""]
# methods is the HTTP method use for request. common method = Get, post, put, delete, 
# -> GET is when you go to the link address, POST is when you submit or send in the information
# data hold all the info of the form post.
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # checking to see if the user is in the database
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True) # store user info in the session
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password, Try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # checking to see if the user already sign up
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        # Checking for the valid sign up information
        # category can be anything, so we can use to edit it later (front-end)
        elif len(email) < 4:
            flash('Email must be greater than 3 character.', category='error')
        elif len(first_name) < 2:
            flash('First Name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('password don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 character.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))

            # adding new_user to database 
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')

            # redirecting back to the home page views is your file and home is the function
            return redirect(url_for('views.home'))


    return render_template("sign_up.html", user=current_user)


