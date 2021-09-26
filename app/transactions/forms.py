from flask.app import Flask
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, SubmitField
from wtforms.fields.core import DateField, IntegerField
from wtforms.validators import (DataRequired, Email, EqualTo, Length,
                                NumberRange, ValidationError)

class SearchForm(FlaskForm):
    name = StringField('Name' , validators = [DataRequired()] )
    search = SubmitField('Search')
    
class IssueForm(FlaskForm):
    b_name = StringField('Book Name' , validators = [DataRequired()])
    m_name = StringField('Member Name' , validators = [DataRequired()])
    # issue_date = DateField('Issue Date' , validators = [DataRequired()])
    rent_period = IntegerField('Rent Period' , validators = [DataRequired()])
    fine = IntegerField('Fine' , validators = [DataRequired()])
    submit = SubmitField('Submit')


