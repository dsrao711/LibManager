from sqlalchemy.orm import backref
from app import db
from app.transactions.models import Transactions

class members(db.Model):
    member_id = db.Column(db.Integer , primary_key = True , unique = True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    contact = db.Column(db.String , unique = True)
    debt = db.Column(db.Integer)
    member_transaction = db.relationship('Transactions' , backref = 'issued_by')
    
db.create_all()