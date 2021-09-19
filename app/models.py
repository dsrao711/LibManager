from app import db

# Members
class Member(db.Model):
   id = db.Column(db.Integer, primary_key =True)
   name = db.Column(db.String(100), nullable = False)
   email = db.Column(db.String(100), nullable= False)
   contact_no = db.Column(db.String(150), nullable = False)
   
#Books
class Books(db.Model):
   book_id = db.Column(db.Integer , primary_key = True)
   title = db.Column(db.String , primary_key = True)
   author = db.Column(db.String , primary_key = True)
   isbn = db.Column(db.String , primary_key = True)
   quantity = db.Column(db.String , primary_key = True)
   
db.create_all()