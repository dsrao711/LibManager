from app import db 

class Transactions(db.Model):

    transaction_id = db.Column(db.Integer , primary_key = True)
    book_name = db.Column(db.String , db.ForeignKey('books.title') )
    smember_name = db.Column(db.String , db.ForeignKey('members.member_id'))
    date = db.Column(db.Date )
    rent_period = db.Column(db.Integer)
    fine = db.Column(db.Integer)
    
    
    
    
    
    
    