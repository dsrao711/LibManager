from re import search
from wtforms import form
from app import db
from flask import Blueprint, redirect, render_template, url_for , flash , request
from app.members.models import members
from app.members.forms import AddMember, SearchMember , EditMember , DeleteMember

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

@bp.route("/members" , methods = ['GET' , 'POST' , 'DELETE'])
def get_members():
    
    users = members.query
    search_form = SearchMember()  
    edit_form = EditMember()
    delete_form = DeleteMember()
    
    # Search for Members
    if search_form.validate_on_submit():
        users = users.filter(members.name.like('%' + search_form.name.data + '%')) 
    users = users.order_by(members.name).all()   
    
    # Edit Member
    if edit_form.validate_on_submit():
        print("Validated edit form")
        print(edit_form.data)
        data = edit_form.data
        del data['csrf_token']
        del data['edit']
        member = members.query.filter_by(member_id = data['member_id']).update(data)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    
    # Delete Member
    if delete_form.validate_on_submit():
        print("Validating Delete...")
        print(delete_form.data)
        data = delete_form.data
        del data['csrf_token']
        del data['delete']
        del_member = members.query.filter_by(member_id = data['member_id']).delete()
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    
    
    return render_template('members/members.html' , users = users , search_form = search_form , edit_form = edit_form , delete_form = delete_form)


        




