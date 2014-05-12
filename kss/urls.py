# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('kss.views',
    url(r'^$', 'home', name='kss_home'),
)

urlpatterns += patterns('',
    url(r'^home/', include('kss.app.home.urls')),
    url(r'^auth/', include('kss.app.auth.urls')),
)

urlpatterns += staticfiles_urlpatterns()
