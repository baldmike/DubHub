# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'playlist_app/index.html')

def playlist_create(request):
    return render(request, 'playlist_app/index.html')

def playlist_view(request):
    return render(request, 'playlist_app/index.html')

def playlist_update(request):
    return render(request, 'playlist_app/index.html')

def playlist_delete(request):
    return render(request, 'playlist_app/index.html')

