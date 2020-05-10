# views.py
from flask import jsonify
from flask import render_template
from back import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/he')
def he():
    return ('<p>A</p>')
