from app import db
from app.transactions.forms import  SearchForm , IssueForm
from flask import Blueprint, flash, redirect, render_template, request, url_for
from app.books.models import Books
from app.members.models import members
from app.transactions.models import Transactions

bp = Blueprint('transactions' , __name__)

@bp.route("/book_issue", methods=['GET', 'POST'])
def book_search():
    search_form = SearchForm()
    issue_form = IssueForm()
    books = Books.query
    
    if search_form.validate_on_submit():
        print("Validating Search ...")
        data = search_form.data
        print(data)
        books = books.filter(Books.title.like('%' + data['name'] + '%')) 
    
    if issue_form.validate_on_submit():
        print("Validating Issue Form ...")
        
        transaction_data = issue_form.data
        del transaction_data['csrf_token']
        del transaction_data['submit']
        print(transaction_data)
        
        member = members.query.filter_by(name = transaction_data['m_name'])
        if member :
            print("Member Found")
            
            # transaction_complete = Transactions(
            #     book_name = transaction_data['b_name'] , 
            #     member_name = transaction_data['m_name'] , 
            #     date = transaction_data['issue_date'] , 
            #     rent_period = transaction_data['issue_date'] , 
            #     fine = transaction_data['fine']
            # )
            # db.session.add(transaction_complete)
            # db.session.commit()      
             
            # transaction_complete = Transactions(**transaction_data)
            # db.session.add(transaction_complete)
            # db.session.commit()
            
        else:
            print("Member not found") 
            
    return render_template('transactions/book_issue.html', title ='Issue Book', search_form = search_form , books = books , issue_form = issue_form)


