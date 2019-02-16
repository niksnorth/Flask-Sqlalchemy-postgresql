from flask import Flask, render_template, request, make_response
from flask_sqlalchemy import SQLAlchemy
from config import app_config

#app = Flask(__name__)
#app.config.from_object(app_config[env_name])

#JWT_SECRET_KEY = hhgaghhgsdhdhdd

def create_app(env_name):
    """
    Create app
    """
    # app initiliazation
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])
    return app
