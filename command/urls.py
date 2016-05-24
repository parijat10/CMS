from django.conf.urls import patterns, url
from command import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^index', views.index, name='indexFull'),
		url(r'^control', views.control, name='control'),
		url(r'^moveBot', views.moveBot, name='moveBot'),
		url(r'^sendCoord', views.sendCoord, name='sendCoord'),	
        )
