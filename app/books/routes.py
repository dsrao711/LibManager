import json
import os
import urllib
import urllib.request

import requests
from app import  db
from app.books.forms import ImportBook, SearchBook
from app.books.models import Books
from flask import Blueprint, redirect, render_template,  url_for


bp =  Blueprint('books' , __name__)


@bp.route("/importbooks" , methods = ["GET" , "POST"])
def add_books():
    form = SearchBook() 
    form_import = ImportBook() 
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
 
    return render_template('books/import_books.html' , form= form  , books = books , form_import = form_import)


@bp.route("/addbook" , methods = ['POST'])
def books():
    print("Adding Book")
    form_import = ImportBook()
    
    if(form_import.validate_on_submit()):
        print("Inside Submit")
        book = Books(
            book_id = form_import.book_id.data  ,
            title = form_import.name.data ,
            author = form_import.author.data ,
            isbn = form_import.isbn.data , 
            quantity = form_import.quantity.data 
        )
        print(form_import.quantity.data) 
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('books.add_books'))
        
    return redirect(url_for('books.add_books'))
            




