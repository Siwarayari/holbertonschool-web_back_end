#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template, g, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def Welcome():
    """basic Flask app"""
    return render_template('5-index.html')


class Config(object):
    """Supported languages list"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """function with the babel.localeselector decorator.
    Use request.accept_languages to determine the best
    match with our supported languages"""
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
    """function that returns a user dictionary or None
    if the ID cannot be found or if login_as was not passed"""
    login_as = request.args.get("login_as")
    if not login_as:
        return None
    else:
        id = int(login_as)
        return users.get(id)


@app.before_request
def before_request():
    """function and use the app.before_request decorator
    to make it be executed before all other functions"""
    g.user = get_user()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
