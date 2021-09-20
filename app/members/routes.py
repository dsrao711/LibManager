import requests

from app import  db
from app.members.models import Members
from flask import Blueprint, redirect, render_template,  url_for

bp = Blueprint('members' , __name__)

@bp.route('/add_member' , methods = ['GET' , 'POST'])
def add_member():
    return render_template('members/add_member.html')


