from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///library.db'

db = SQLAlchemy(app)
db.create_all()

from app.books.routes import bp as books_blueprint
from app.main.routes import bp as main_blueprint
from app.members.routes  import bp as members_blueprint

app.register_blueprint(books_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(members_blueprint)


