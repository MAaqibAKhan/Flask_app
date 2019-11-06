from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.220.165.221/GuessTheWorld'
db=SQLAlchemy(app)

app.config['SECRET_KEY'] = '7C51196E8E17EA9DB3AFD4AB8E4F3'

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application import routes
