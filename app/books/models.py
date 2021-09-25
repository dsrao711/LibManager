from app.transactions.models import Transactions
from app import db
from app.transactions.models import Transactions
class Books(db.Model):
       
   book_id = db.Column(db.Integer , primary_key = True)
   title = db.Column(db.String)
   author = db.Column(db.String)
   isbn = db.Column(db.String)
   quantity = db.Column(db.String)
   book_transactions = db.relationship('Transactions' , backref = 'book_issued')
   
db.create_all()