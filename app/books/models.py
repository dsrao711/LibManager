from app import db

class Books(db.Model):
   book_id = db.Column(db.Integer , primary_key = True)
   title = db.Column(db.String , primary_key = True)
   author = db.Column(db.String , primary_key = True)
   isbn = db.Column(db.String , primary_key = True)
   quantity = db.Column(db.String , primary_key = True)
   
