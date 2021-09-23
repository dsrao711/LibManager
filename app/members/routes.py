from re import search
from wtforms import form
from app import db
from flask import Blueprint, redirect, render_template, url_for , flash
from app.members.models import members
from app.members.forms import AddMember, SearchMember

bp = Blueprint('members' , __name__)

@bp.route("/register", methods=['GET', 'POST'])
def register():
    form = AddMember()
    
    if form.validate_on_submit():
        user = members(member_id = form.member_id.data , name = form.name.data , email=form.email.data, contact = form.contact.data , debt = 0)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('members.register'))
    
    return render_template('members/add_member.html', title='Add Member', form=form)

@bp.route("/members" , methods = ['GET' , 'POST'])
def get_members():
    users = members.query
    search_form = SearchMember()  
    if search_form.validate_on_submit():
        users = users.filter(members.name.like('%' + search_form.name.data + '%')) 
    users = users.order_by(members.name).all()
    
    return render_template('members/members.html' , users = users , search_form = search_form)


