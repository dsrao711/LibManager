from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

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
from app.transactions.routes  import bp as transactions_blueprint

app.register_blueprint(books_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(transactions_blueprint)


