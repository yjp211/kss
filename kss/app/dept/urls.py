# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from kss.app.dept.views import dept

urlpatterns = patterns('',
    url(r'^$', dept.index, name='dept_index'),
)
