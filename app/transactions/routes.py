from app import db
from app.transactions.forms import  SearchForm , IssueForm
from flask import Blueprint, flash, redirect, render_template, request, url_for
from app.books.models import Books
from app.members.models import members
from app.transactions.models import Transactions

bp = Blueprint('transactions' , __name__)

@bp.route("/book_issue", methods=['GET', 'POST'])
def book_issue():
    search_form = SearchForm()
    issue_form = IssueForm()
    books = Books.query
    
    if search_form.validate_on_submit():
        print("Validating Search ...")
        data = search_form.data
        print(data)
        books = books.filter(Books.title.like('%' + data['name'] + '%')) 
        
    if issue_form.validate_on_submit():
        
        print("Validating Issue Form")
        issue_form_data = issue_form.data
        print()
        print(issue_form_data)
        member = members.query.filter_by (name = issue_form_data['m_name'])
        
        if member :
            print('Member found')
        else:
            print('Member not found. Please register the new member')
            
    return render_template('transactions/book_issue.html', title ='Issue Book', search_form = search_form , books = books , issue_form = issue_form)

