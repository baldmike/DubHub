from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.user_app.urls'))
    # url(r'^music/', include('apps.music_app.urls', namespace='music')),
    # url(r'^playlist/', include('apps.playlist_app.urls', namespace='playlist'))
]

    