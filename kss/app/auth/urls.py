# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from kss.app.auth.views import auth

urlpatterns = patterns('',
    url(r'^login/$', auth.index, name='login_index'),
    url(r'^login/action/$', auth.action, name='login_action'),
)
