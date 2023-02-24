# Storing routes for our website, mostly for the home page (website look)
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json


# a bunch of url link into views
views = Blueprint('views', __name__)

# URL to get to the end poing of route 
@views.route('/', methods=['GET', 'POST'])
@login_required # can't get into home page unless you're login
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        # checking to see if you can add the note
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId= note['noteId']
    note = Note.query.get(noteId)

    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})