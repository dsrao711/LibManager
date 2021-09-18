from flask_wtf import FlaskForm
from wtforms import Form,StringField, validators
from wtforms.fields.core import IntegerField

class AddBooks(FlaskForm):
    title = StringField('title')
    author = StringField('author')
    isbn = StringField('isbn')
    
    