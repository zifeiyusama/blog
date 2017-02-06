#/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    blog.urls
    ~~~~~~~~~~~~~~

    url patterns for blog

    :copyright: (c) 2016 by zifeiyu.
    :license: MIT, see LICENSE for more details.
"""
from django.conf.urls import url, include

from .import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.articles, name='index'),
    url(r'^articles/column/(?P<column>.*)$', views.articles, name='column'),
    url(r'^articles/archive/(?P<archive>[0-9]{6})$', views.articles, name='archive'),
    url(r'^articles/tag/(?P<tag>.*)$', views.articles, name='tag'),
    url(r'^articles$', views.articles, name='articles'),
    url(r'^article/(?P<article>.*)$', views.article, name='article'),
    url(r'^about$', views.about, name='about'),
    url(r'^wiki$', views.wiki, name='wiki')
]
