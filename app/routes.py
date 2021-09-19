from typing import _SpecialForm
import requests , urllib , json
from wtforms import validators
from app import app , db
from flask import render_template , redirect , url_for , request
from app.forms import SearchBook
import urllib.request, json ,os , requests

@app.route("/")
def dashboard():
    return render_template('dashboard.html')

@app.route("/importbooks" , methods = ["GET" , "POST"])
def add_books():
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
        
    return render_template('books/import_books.html' , form= form  , books = books)


