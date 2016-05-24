from django.conf.urls import patterns, url
from status import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^index', views.index, name='indexFull'),
		url(r'^main', views.main, name="main"),
		url(r'^view', views.view, name="view"),
		url(r'^read_coordinates', views.read_coordinates, name="rc"),
		url(r'^getImage', views.getImage, name="gi"),
        )
