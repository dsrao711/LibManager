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
            values['title'] = self.title.data
        if(self.author != None):
            values['author'] = self.author.data
        if(self.isbn != ''):
            values['isbn'] = self.isbn.data
        return values
            
            
    

    
    