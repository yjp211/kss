# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from kss.app.auth.views import auth

urlpatterns = patterns('',
    url(r'^login/$', auth.index, name='login_index'),
    url(r'^login/action/$', auth.login_in, name='login_action'),
    url(r'^login/login_out/$', auth.login_out, name='login_out'),
)
