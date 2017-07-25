from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login, name='login_reg_login'),
    url(r'^register$', views.register, name='login_reg_register'),
    url(r'^success$', views.success, name='login_reg_success'),
    url(r'^reset$', views.reset, name='login_reg_reset'),
    url(r'^update$', views.update_user),
    url(r'^delete$', views.delete_user),
]