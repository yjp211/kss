# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('kss.app.auth.views',
    url(r'^login/$', 'index', name='login_index'),
    url(r'^login/action/$', 'action', name='login_action'),
)
