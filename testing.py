import pdb # pdb.set_trace()
import unittest
from flask import Flask
import random
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from model import db, app, InventoryItem
import config 
#from model import app, db
#from model import Participant, Session

class TestInventory(unittest.TestCase):
    def setUp(self):
        #app.config.from_object('app.config.Testing')
        app = Flask(__name__)
        app = create_app('testing')
        
        #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db = SQLAlchemy(app)
        db.session.close()
        db.drop_all()
        db.create_all()

    def test_lookup(self):
        tinventory = InventoryItem('106', 'Ponting' , 111.001)
        db.session.add(tinventory)
        #db.session.commit()
        tinventories = db.session.query(InventoryItem).all()
        #assert tinventory in tinventories
        assert tinventory in InventoryItem
        print("NUMBER OF ENTRIES:")
        print(len(tinventories))


if __name__ == '__main__':
    unittest.main()