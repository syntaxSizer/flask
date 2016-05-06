from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/')
@app.route('/about')
def about():
    print 'to the backend world '
    print 'like it or not, its not going to be esy'
    
    return render_template("about.html",
                           title='About')

@app.route('/')
@app.route('/TMT')
def TMT():
    print 'Anouther boaring page '
    return render_template("TMT.html",
                          title='TMT')
