
from flask import Blueprint, flash, redirect, render_template, request, url_for

bp = Blueprint('transactions' , __name__)

@bp.route("/book_issue" , methods = ['GET' , 'POST'])
def book_issue():
    return render_template("transactions/book_issue.html")