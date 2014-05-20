# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from kss.app.org.views import org

urlpatterns = patterns('',
    url(r'^$', org.index, name='org_index'),
)
