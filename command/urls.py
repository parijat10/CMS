
from django.conf.urls import patterns, url, include
from command import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^index', views.index, name='indexFull'),
		url(r'^control', views.control, name='control'),
		url(r'^moveBot', views.moveBot, name='moveBot'),
        )

# urlpatterns += [
#     url("", include('django_socketio.urls')),
# ]