from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^playlist_create$', views.playlist_create),
    url(r'^playlist_view$', views.playlist_view),
    url(r'^playlist_update$', views.playlist_update),
    url(r'^playlist_delete$', views.playlist_delete),
]
