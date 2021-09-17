import requests , urllib , json
from app import app , db
from flask import render_template

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/getbooks")
def get_books():
    # Fetch books from frape api
    url = "https://frappe.io/api/method/frappe-library"
    response = urllib.request.urlopen(url)
    data=response.read()
    dict_ = json.loads(data)
    print(dict_)
    return render_template('get_books.html' , books = dict_)
