from app import db
class Books(db.Model):
   book_id = db.Column(db.Integer , primary_key = True)
   title = db.Column(db.String)
   author = db.Column(db.String)
   isbn = db.Column(db.String)
   quantity = db.Column(db.String)
   
db.create_all()