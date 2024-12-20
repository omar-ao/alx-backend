#!/usr/bin/env python3
"""
app
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    Config
    """
    LANGUAGES = ["en", "fr"]
    LANGUAGES_DEFAULT = "en"
    TIMEZONE_DEFAULT = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """
    index
    """
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """
    get_locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
