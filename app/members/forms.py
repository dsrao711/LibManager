from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError , NumberRange

class AddMember(FlaskForm):
    member_id = StringField('ID' , validators=[Length(min = 4 , max = 5)])
    name = StringField('Name' , validators=[DataRequired()])
    email = StringField('Email' , validators=[DataRequired() , Email()])
    contact = StringField('Contact' , validators=[DataRequired() , Length(min = 10, max = 10)])
    add = SubmitField('Add member')
    
class SearchMember(FlaskForm):
    name = StringField('Name' , validators=[DataRequired()] )
    search = SubmitField('Search')
    