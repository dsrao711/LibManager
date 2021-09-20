import requests

from app import  db
from app.books.forms import ImportBook, SearchBook
from app.books.models import Books
from flask import Blueprint, redirect, render_template,  url_for

bp =  Blueprint('books' , __name__)

@bp.route("/books_search" , methods = ["GET" , "POST"])
def add_books():
    form_filter = SearchBook() 
    form_import = ImportBook() 
    jsonData = []
    books = []
    if(form_filter.validate_on_submit()):
        values = form_filter.getdata()         
        r = requests.get('https://frappe.io/api/method/frappe-library' , params = values)
        jsonData = r.json()
        for value in jsonData['message']:
            books.append([value['bookID'],value['title'] , value['authors'] , value['isbn']])
 
    return render_template('books/books_import.html' , form_filter = form_filter  , books = books , form_import = form_import)


@bp.route("/books_import" , methods = ['POST'])
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
            




