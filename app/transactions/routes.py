from app import db
from app.transactions.forms import IssueForm, SearchForm
from flask import Blueprint, flash, redirect, render_template, request, url_for
from app.books.models import Books

bp = Blueprint('transactions' , __name__)

@bp.route("/book_issue", methods=['GET', 'POST'])
def book_issue():
    search_form = SearchForm()
    issue_form = IssueForm()
    books = Books.query
    
    if search_form.validate_on_submit():
        print("Validating Search ...")
        data = search_form.data
        books = books.filter(Books.title.like('%' + data['name'] + '%')) 
    
    return render_template('transactions/book_issue.html', title ='Issue Book', search_form = search_form , books = books , issue_form = issue_form)

