# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *

def index(request):
    context={
        'artists': Artist.objects.all()
    }
    return render(request, 'music_app/index.html', context)

def artist_create(request):
    if request.method == 'POST':
        artist_name= request.POST['artist_name']
        artist_bio= request.POST['artist_bio']
        Artist.objects.create(artist_name=artist_name, artist_bio=artist_bio)
    return redirect('music_app:index')

def addArtist(request):
    return render(request, 'music_app/addArtist.html')
    
    

def artist_view(request, id):
    context={
        'artist': Artist.objects.get(id=id)
    }
    return render(request, 'music_app/displayArtist.html', context)

def editArtist(request, id):
    context={
        'artist': Artist.objects.get(id=id)
    }
    return render(request, 'music_app/editArtist.html', context)

def artist_update(request, id):
    artist = Artist.objects.get(id=id)
    artist.artist_name= request.POST['artist_name']
    artist.artist_bio= request.POST['artist_bio']
    artist.save()
    return redirect('music_app:index')

def artist_delete(request, id):
    artist = Artist.objects.get(id=id)
    artist.delete()
    return redirect('music_app:index')

# ************************
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