# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('kss.app.home.views',
    url(r'^$', 'home', name='kss_home'),
)
