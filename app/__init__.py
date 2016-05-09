import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models, app


lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
