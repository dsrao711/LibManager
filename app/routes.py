from typing import _SpecialForm
import requests , urllib , json

from wtforms import validators
from app import app , db
from flask import render_template , redirect , url_for , request
from app.forms import SearchBook

@app.route("/")
def dashboard():
    return render_template('dashboard.html')


@app.route("/importbooks" , methods = ["GET" , "POST"])
def add_books():
    form = SearchBook()  

    if(form.validate_on_submit()):
        
        print(form.title.data)
        return redirect(url_for('add_books'))
    
    return render_template('books/import_books.html' , form= form)
    
    


