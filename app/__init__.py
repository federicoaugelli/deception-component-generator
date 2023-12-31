from flask import Flask

from .extensions import api, db
from .resources import ns 
from .models import *

def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../database/centraldb.sqlite3'

    api.init_app(app)
    db.init_app(app)

    api.add_namespace(ns)

    #############################################

    return app