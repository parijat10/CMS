from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RobotCMS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'authorize.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^authorize/', include('authorize.urls')),
    url(r'^status/', include('status.urls')),
    url(r'^command/', include('command.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
	{'document_root': settings.MEDIA_ROOT}), )
