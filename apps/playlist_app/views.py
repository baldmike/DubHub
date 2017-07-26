# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from models import *

# Create your views here.
def addPlaylist(request):

    return render(request, 'playlist_app/addPlaylist.html')

def createPlaylist(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        playlist_name = request.POST['playlist_name']
        Playlist.objects.create(playlist_name=playlist_name, user_id=user_id)
        playlist_id = Playlist.objects.get(id=playlist_id)

    return redirect('music_app:index')
    
def viewPlaylist(request, playlist_id):
    context={
        'playlist': Playlist.objects.get(id=playlist_id),
    }
    return render(request, 'playlist_app/viewPlaylist.html', context)

def addToPlaylist(request, song_id):
    playlistSong= Song.objects.get(id=song_id)

    return render(request, 'playlist_app/viewPlaylist.html')




def playlist_create(request):
    return render(request, 'playlist_app/index.html')

def playlist_update(request):
    return render(request, 'playlist_app/index.html')

def playlist_delete(request):
    return render(request, 'playlist_app/index.html')

