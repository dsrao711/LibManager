import requests , urllib , json
from app import app , db
from flask import render_template
from app.forms import AddBooks

@app.route("/")
def dashboard():
    return render_template('index.html')


@app.route("/importbooks" , methods = ["GET" , "POST"])
def add_books():
    # Fetch books from frape api
    url = "https://frappe.io/api/method/frappe-library?"

    return render_template('books/import_books.html')
