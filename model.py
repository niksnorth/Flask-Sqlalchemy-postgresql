from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import class_mapper, ColumnProperty
import sqlalchemy
from datetime import datetime
from app import create_app

env_name = 'production'
app = create_app(env_name)
db = SQLAlchemy(app)


class InventoryItem(db.Model):
    """Base data model for all objects"""
    __tablename__ = 'inventory'
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    price = db.Column(db.Float)

    #----------------------------------------------------------------------
    def __init__(self, id, name, price):
        """  initialisation """
        self.id = id
        self.name = name
        self.price = price

    #----------------------------------------------------------------------
    def __repr__(self):
        """ Define a base way to print models """
        return f"inventory('{self.id}', '{self.name}', '{self.price}')" 