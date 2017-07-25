from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^user_app/update_user$', views.update_user),
    url(r'^user_app/delete_user$', views.delete_user),
]