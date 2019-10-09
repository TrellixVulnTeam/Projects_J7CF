from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '88d6c92e131869aa1f3d25badaf83d69'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/games.db'
db = SQLAlchemy(app)

from flaskwsite import routes
