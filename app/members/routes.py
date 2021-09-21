import requests

from app import  db
from app.members.models import Members
from flask import Blueprint, redirect, render_template,  url_for
from app.members.forms import AddMember

bp = Blueprint('members' , __name__)

@bp.route('/add_member' , methods = ['GET' , 'POST'])
def add_member():
    form_add_member = AddMember()
    print("Adding Member")
    if(form_add_member.validate_on_submit()):
        print("Inside submit")
        data = form_add_member.data
        print(data)
        return redirect(url_for(''))
        
    return render_template('members/add_member.html' , form_add_member = form_add_member)

@bp.route('/view_members' , method = ['GET' , 'POST'])
def get_books():
    return render_template('members/members.html')



