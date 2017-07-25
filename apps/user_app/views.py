from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import strftime, localtime
from django.core.urlresolvers import reverse

from models import *

def index(request):
    
    return render(request, 'user_app/index.html')

def register(request):

    errors = User.objects.registration_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.add_message(request, messages.ERROR, errors[tag])
        return redirect("/")
    else:
        first_name =  request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
 
        user = User.objects.create_user(first_name, last_name, email, hashed_password)

        if not user:
            messages.add_message(request, messages.ERROR, "User email already exists.")
            return redirect("/")
        else:
            request.session['first_name'] = first_name
            request.session['last_name'] = last_name
            request.session['email'] = email
            request.session['password'] = hashed_password
            return redirect('/success')

def login(request):
    try:
        user = User.objects.login_validator(request.POST)

        if user:
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            request.session['email'] = user.email
            request.session['password'] = user.password
            return redirect('/success')
        else:
            messages.add_message(request, messages.ERROR, "Invalid login info.")
            return redirect("/")
    except:
        messages.add_message(request, messages.ERROR, "Not in database")
        return redirect('/')
def success(request):

    context = {

        "first_name": request.session['first_name'],
        "last_name": request.session['last_name'],
        "email": request.session['email'],
        "password": request.session['password'],

    }
    return render(request, 'user_app/success.html', context)

def reset(request):
    request.session.flush()
    return redirect('/')

def update_user(request):
    return render(render, 'user_app/index.html')

def delete_user(request):
    return render(render, 'user_app/index.html')
    