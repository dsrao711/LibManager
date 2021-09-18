from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class SearchBook(FlaskForm):
    
    title = StringField('title' , validators=[DataRequired()])
    author = StringField('author')
    isbn = StringField('isbn')
    search = SubmitField('Search')
    
    def getdata(self):
        values = {}
        if(self.title != None):
            values['title'] = self.title
        if(self.author != None):
            values['author'] = self.author
        if(self.isbn != None):
            values['isbn'] = self.isbn
        return values
            
            
    

    
    