# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from kss.app.org.views import org

urlpatterns = patterns('',
    url(r'^$', org.index, name='org_index'),

    url(r'^load_root/$', org.load_root, name='org_load_root'),
    url(r'^load_dept/$', org.load_dept, name='org_load_dept'),
)
