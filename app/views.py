from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

@app.route('/')
@app.route('/about')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('about.html',
                           title='About',
                           user=user)

@app.route('/')
@app.route('/TMT.html')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('TMT.html',
                           title='TM',
                           user=user)
