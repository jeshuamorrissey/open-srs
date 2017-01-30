from srs import app
from srs.models.deck import Deck

from flask import render_template
from flask_stormpath import login_required, user


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/decks')
@login_required
def decks():
  return render_template('decks.html')
