#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template
from flask_babel import Babel, refresh

app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def Welcome():
    """basic Flask app"""
    return render_template('0-index.html')


class Config(object):
    """Supported languages list"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
