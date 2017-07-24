from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^artist_create$', views.artist_create),
    url(r'^artist_view$', views.artist_view),
    url(r'^artist_update$', views.artist_update),
    url(r'^artist_delete$', views.artist_delete),
    url(r'^album_create$', views.album_create),
    url(r'^album_view$', views.album_view),
    url(r'^album_update$', views.album_update),
    url(r'^album_delete$', views.album_delete),
    url(r'^song_create$', views.song_create),
    url(r'^song_view$', views.song_view),
    url(r'^song_update$', views.song_update),
    url(r'^song_delete$', views.song_delete),
    url(r'^search$', views.search),
    url(r'^new_release$', views.new_release),

]