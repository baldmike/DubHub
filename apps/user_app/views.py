from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import strftime, localtime
from django.core.urlresolvers import reverse
 
from models import *

def index(request):
    return render(request, 'user_app/index.html')

def login(request):
    return render(request, 'user_app/index.html')

def register(request):
    return render(render, 'user_app/index.html')

def update_user(request):
    return render(render, 'user_app/index.html')

def delete_user(request):
    return render(render, 'user_app/index.html')
    