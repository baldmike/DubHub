# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
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
    

def artist_view(request, artist_id):
    context={
        'artist': Artist.objects.get(id=artist_id)
    }
    return render(request, 'music_app/displayArtist.html', context)

def artist_edit(request, id):
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

def addAlbum(request, artist_id):
    context={
        'artist': Artist.objects.get(id=artist_id)
    }
    return render(request, 'music_app/albumCreate.html', context)
    

def album_create(request, id):
    if request.method == 'POST':
        artist= Artist.objects.get(id=id)
        album_name= request.POST['album_name']
        album_year= request.POST['album_year']
        Album.objects.create(album_name= album_name, album_year= album_year, artists=artist)
    
    return redirect(reverse('music_app:viewArtist', kwargs={'artist_id': id}))

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