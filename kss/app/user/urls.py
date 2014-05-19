# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from kss.app.user.views import user

urlpatterns = patterns('',
    url(r'^$', user.index, name='user_index'),
)
