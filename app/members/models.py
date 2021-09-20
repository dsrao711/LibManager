from app import db 

class Members(db.Model):
    member_id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    contact = db.Column(db.String , unique = True)
    
    