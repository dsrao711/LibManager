import requests

from app import  db
from app.books.forms import ImportBook, SearchBook
from app.books.models import Books
from flask import Blueprint, redirect, render_template,  url_for

bp =  Blueprint('books' , __name__)

@bp.route("/books_search" , methods = ["GET" , "POST"])
def search_books():
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
def import_books():
    print("Adding Book")
    form_import = ImportBook()
    
    if(form_import.validate_on_submit()):
        print("Inside Submit")
        if(db.session.query(Books).filter_by(book_id = form_import.book_id.data).count() < 1):
            book = Books(
            book_id = form_import.book_id.data  ,
            title = form_import.name.data ,
            author = form_import.author.data ,
            isbn = form_import.isbn.data , 
            quantity = form_import.quantity.data)
            db.session.add(book)
            db.session.commit()
        return redirect(url_for('books.search_books'))
        
    return redirect(url_for('books.search_books'))
            

@bp.route("/books_available" , methods = ['GET'])
def get_books():
    books = Books.query.all()
    return render_template('books/books_available.html' , books = books )
