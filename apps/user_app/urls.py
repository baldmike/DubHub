from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^update_user$', views.update_user),
    url(r'^delete_user$', views.delete_user),
]