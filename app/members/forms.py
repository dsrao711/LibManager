from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError , NumberRange

class AddMember(FlaskForm):
    name = StringField('Name' , validators=[DataRequired()])
    email = StringField('Email' , validators=[DataRequired , Email()])
    contact = StringField('Contact' , validators=[DataRequired , Length(min = 10, max = 10)])