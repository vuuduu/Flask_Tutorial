# Storing routes for our website (website look)
from flask import Blueprint, render_template

# a bunch of url link into views
views = Blueprint('views', __name__)

# URL to get to the end poing of route 
@views.route('/')
def home():
    return render_template("home.html")
