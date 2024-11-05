#!/usr/bin/env python3
"""
app
"""
from flask import Flask, render_template
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
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
