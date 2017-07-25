from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^createArtist$', views.createArtist, name='createArtist'),
    url(r'^addArtist$', views.addArtist, name='addArtist'),
    url(r'^(?P<artist_id>\d+)/viewArtist$', views.viewArtist, name='viewArtist'),
    url(r'^(?P<id>\d+)/updateArtist$', views.updateArtist, name='updateArtist'),
    url(r'^(?P<id>\d+)/editArtist$', views.editArtist, name='editArtist'),
    url(r'^(?P<id>\d+)/deleteArtist$', views.deleteArtist, name='deleteArtist'),
    url(r'^(?P<artist_id>\d+)/addAlbum$', views.addAlbum, name='addAlbum'),
    url(r'^(?P<id>\d+)/createAlbum$', views.createAlbum, name='createAlbum'),
    url(r'^viewAlbum$', views.view, name='viewAlbum'),
    url(r'^album_update$', views.album_update, name='updateAlbum'),
    url(r'^album_delete$', views.album_delete, name='deleteAlbum'),
    url(r'^song_create$', views.song_create, name='createSong'),
    url(r'^song_view$', views.song_view, name='viewSong'),
    url(r'^song_update$', views.song_update, name='updateSong'),
    url(r'^song_delete$', views.song_delete, name='deleteSong'),
    url(r'^search$', views.search, name='search'),
    url(r'^new_release$', views.new_release, name='newRelease'),
    
]