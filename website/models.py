# creating the database model
# database model is a blueprint for an object that'll be store in your database
# importing the current package (website folder) and getting the db object
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # letting sql alchemy getting the time for us
    # Must pass valid id of an existing user to the user_id (one user to many notes). User = user and id = id (in the User class)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# defining the user object schema
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) # no other user can have the same email
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # tell flask/sqlalchemy to add note id into the relationship everytime we create it. 
    notes = db.relationship('Note')