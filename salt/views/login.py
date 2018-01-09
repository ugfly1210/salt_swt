from flask import Flask,Blueprint,request,render_template,redirect
from salt import forms

login = Blueprint('login',__name__)

@login.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        form = forms.LoginForm()
        return render_template('login.html',form=form)