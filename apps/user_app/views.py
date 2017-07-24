from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import strftime, localtime
from django.core.urlresolvers import reverse
 
from models import *

def index(request):

    return render(request, 'user_app/index.html')