from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import IntegerField
from wtforms.validators import (DataRequired, Email, EqualTo, Length,
                                NumberRange, ValidationError)

    
class SearchForm(FlaskForm):
    name = StringField('Name' , validators = [DataRequired()] )
    search = SubmitField('Search')
    
