from typing import _SpecialForm
import requests , urllib , json ,os , urllib.request
from wtforms import validators
from flask import render_template , redirect , url_for , request

#app
from app import app , db
#Forms
from app.forms import SearchBook , ImportBook
# Models
from app.models import Books , Member


@app.route("/")
def dashboard():
    return render_template('dashboard.html')

@app.route("/importbooks" , methods = ["GET" , "POST"])
def add_books():
    
    form_import = ImportBook()
    form = SearchBook()  
    jsonData = []
    books = []
    
    if(form.validate_on_submit()):
        # Dict of values from search
        values = form.getdata()
        # Passing Params 
        r = requests.get('https://frappe.io/api/method/frappe-library' , params = values)
        # Printing response from API
        jsonData = r.json()
        # Storing the required info in a list
        for value in jsonData['message']:
            books.append([value['bookID'],value['title'] , value['authors'] , value['isbn']])
            
    if(form_import.validate_on_submit()):
            book = Books(
                book_id = form_import.book_id.data  ,
                title = form_import.name.data ,
                author = form_import.author.data ,
                isbn =form_import.isbn.data , 
                quantity = form_import.quantity.data 
            )
              
            print(form_import.quantity.data) 
            db.session.add(book)
            db.session.commit()
            
            redirect(url_for('add_books'))
            
            
    return render_template('books/import_books.html' , form= form  , books = books , form_import = form_import)







