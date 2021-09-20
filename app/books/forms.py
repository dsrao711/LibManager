from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError , NumberRange

class SearchBook(FlaskForm):
    
    title = StringField('title' , validators=[DataRequired()])
    author = StringField('author')
    isbn = StringField('isbn')
    search = SubmitField('Search')
    
    def getdata(self):
        values = {}
        if(self.title != None):
            values['title'] = self.title.data
        if(self.author != None):
            values['author'] = self.author.data
        if(self.isbn != ''):
            values['isbn'] = self.isbn.data
        return values
    
class ImportBook(FlaskForm):
    
    book_id = StringField('Book ID' , validators=[DataRequired()] )
    name = StringField('Name of the Book' , validators=[DataRequired()] )
    author = StringField('Author' , validators=[DataRequired()])
    isbn = StringField('ISBN', validators=[DataRequired()])
    quantity = IntegerField('Quantity' , validators=[DataRequired() , NumberRange(min=1)] )
    import_books = SubmitField('Import')            

            
    

    
    