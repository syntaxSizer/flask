from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
#we are creating DB object 'db' that will be our DB
db = SQLAlchemy(app)

from app import views, models
