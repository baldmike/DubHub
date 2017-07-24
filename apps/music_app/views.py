# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'music_app/index.html')

def artist_create(request):
    return render(request, 'playlist_app/index.html')

def artist_view(request):
    return render(request, 'playlist_app/index.html')

def artist_update(request):
    return render(request, 'playlist_app/index.html')

def artist_delete(request):
    return render(request, 'playlist_app/index.html')

# ************************


def album_create(request):
    return render(request, 'playlist_app/index.html')

def album_view(request):
    return render(request, 'playlist_app/index.html')

def album_update(request):
    return render(request, 'playlist_app/index.html')

def album_delete(request):
    return render(request, 'playlist_app/index.html')


# ************************


def song_create(request):
    return render(request, 'playlist_app/index.html')

def song_view(request):
    return render(request, 'playlist_app/index.html')

def song_update(request):
    return render(request, 'playlist_app/index.html')

def song_delete(request):
    return render(request, 'playlist_app/index.html')

# ************************


def search(request):
    return render(request, 'playlist_app/index.html')

def new_release(request):
    return render(request, 'playlist_app/index.html')