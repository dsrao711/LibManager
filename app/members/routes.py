import requests

from app import  db
from app.members.models import Members
from flask import Blueprint, redirect, render_template,  url_for
from app.members.forms import AddMember

bp = Blueprint('members' , __name__)

@bp.route('/add_member' , methods = ['GET' , 'POST'])
def add_member():
    
    form_add_member = AddMember()
    print("Adding Member..")
    if(form_add_member.validate_on_submit()):
        print("Inside submit..")
        
        data = form_add_member.data
        del data['csrf_token']
        
        print(data)
        member = Members(
            member_id = data['member_id'],
            name = data['name'] , 
            email = data['email'] , 
            contact = data['contact']
        )
        db.session.add(member)
        db.session.commit()
        
        return redirect(url_for('members.add_member'))
        
    return render_template('members/add_member.html' , form_add_member = form_add_member)


@bp.route('/view_members' , methods = ['GET' , 'POST'])
def get_members():
    # Query all members
    
    
    return render_template('members/members.html')



