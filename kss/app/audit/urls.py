# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from kss.app.audit.views import audit

urlpatterns = patterns('',
    url(r'^$', audit.index, name='audit_index'),
)
