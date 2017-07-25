from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^artist_create$', views.artist_create, name='createArtist'),
    url(r'^addArtist$', views.addArtist, name='addArtist'),
    url(r'^(?P<id>\d+)/artist_view$', views.artist_view, name='viewArtist'),
    url(r'^(?P<id>\d+)/artist_update$', views.artist_update, name='updateArtist'),
    url(r'^(?P<id>\d+)/artist_edit$', views.artist_edit, name='editArtist'),
    url(r'^(?P<id>\d+)/artist_delete$', views.artist_delete, name='deleteArtist'),
    url(r'^album_create$', views.album_create, name='createAlbum'),
    url(r'^album_view$', views.album_view, name='viewAlbum'),
    url(r'^album_update$', views.album_update, name='updateAlbum'),
    url(r'^album_delete$', views.album_delete, name='deleteAlbum'),
    url(r'^song_create$', views.song_create, name='createSong'),
    url(r'^song_view$', views.song_view, name='viewSong'),
    url(r'^song_update$', views.song_update, name='updateSong'),
    url(r'^song_delete$', views.song_delete, name='deleteSong'),
    url(r'^search$', views.search, name='search'),
    url(r'^new_release$', views.new_release, name='newRelease'),
    
]