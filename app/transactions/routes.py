
from flask import Blueprint, flash, redirect, render_template, request, url_for
from app.transactions.forms import SearchForm

bp = Blueprint('transactions' , __name__)

@bp.route("/book_issue", methods=['GET', 'POST'])
def book_issue():
    
    search_form = SearchForm()
    if search_form.validate_on_submit():
        print("Validating Search ...")
    return render_template('transactions/book_issue.html', title ='Issue Book', search_form = search_form)