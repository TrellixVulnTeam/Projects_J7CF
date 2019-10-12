from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:guccio2016@localhost/height_collector_2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fhwrjyijjnqinj:30cb75928433b33f67723f35986353f29c8d5f243d664fe3a7fec0c280b43972@ec2-54-247-170-5.eu-west-1.compute.amazonaws.com:5432/d1phnis3vcjqpt?' \
                                        'sslmode=require'
app.config['SECRET_KEY'] = '88d6c92e131869aa1f3d25badaf83d69'
db = SQLAlchemy(app)

from datacollector import routes
