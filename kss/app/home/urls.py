# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from kss.app.home.views import home

urlpatterns = patterns('',
    url(r'^$', home.index, name='home_index'),
)
