from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^createArtist$', views.createArtist, name='createArtist'),
    url(r'^addArtist$', views.addArtist, name='addArtist'),
    url(r'^(?P<artist_id>\d+)/viewArtist$', views.viewArtist, name='viewArtist'),
    url(r'^(?P<artist_id>\d+)/updateArtist$', views.updateArtist, name='updateArtist'),
    url(r'^(?P<artist_id>\d+)/editArtist$', views.editArtist, name='editArtist'),
    url(r'^(?P<artist_id>\d+)/deleteArtist$', views.deleteArtist, name='deleteArtist'),
    url(r'^(?P<artist_id>\d+)/addAlbum$', views.addAlbum, name='addAlbum'),
    url(r'^(?P<artist_id>\d+)/createAlbum$', views.createAlbum, name='createAlbum'),
    url(r'^(?P<album_id>\d+)/viewAlbum$', views.viewAlbum, name='viewAlbum'),
    url(r'^(?P<album_id>\d+)/updateAlbum$', views.updateAlbum, name='updateAlbum'),
    url(r'^(?P<album_id>\d+)/deleteAlbum$', views.deleteAlbum, name='deleteAlbum'),
    url(r'^createSong$', views.createSong, name='createSong'),
    url(r'^viewSong$', views.viewSong, name='viewSong'),
    url(r'^updateSong$', views.updateSong, name='updateSong'),
    url(r'^deleteSong$', views.deleteSong, name='deleteSong'),
    url(r'^search$', views.search, name='search'),
    
]