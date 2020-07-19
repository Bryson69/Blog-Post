from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# "Import flask and render template ,
app = Flask(__name__)# app is a flask variable whihc is set to an instance ,Add flask variable,
app.config['SECRET_KEY'] = 'c7f3e00d51e9c47c506c8d05ec7d027d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes