# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('kss.views',
    url(r'^$', 'home', name='kss_home'),
)

urlpatterns += patterns('',
    url(r'^home/', include('kss.app.home.urls')),
    url(r'^auth/', include('kss.app.auth.urls')),
    url(r'^audit/', include('kss.app.audit.urls')),
    url(r'^backup/', include('kss.app.backup.urls')),
    url(r'^dept/', include('kss.app.dept.urls')),
    url(r'^police/', include('kss.app.police.urls')),
    url(r'^user/', include('kss.app.user.urls')),
)

urlpatterns += staticfiles_urlpatterns()
