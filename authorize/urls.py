from django.conf.urls import patterns, url
from authorize import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^index', views.index, name='indexFull'),
		url(r'^user_logout', views.user_logout, name='logout'),
        )
