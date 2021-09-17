import requests
import json
from flaskapp import app , db
from flask import render_template

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/getbooks")
def get_books():
    url = "https://frappe.io/api/method/frappe-library?"
    
    
    return render_template('get_books.html')
