#/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    blog.views
    ~~~~~~~~~~~~~~

    customize and cache context processors

    :copyright: (c) 2016 by zifeiyu.
    :license: MIT, see LICENSE for more details.
'''
from .models import Column, Tag, Archive
from django.conf import settings

def columns(request):
    columns = Column.objects.filter(article__status='PUBLISHED').distinct()
    return {'columns': columns}

def tags(request):
    tags = Tag.objects.filter(article__status='PUBLISHED').distinct()
    return {'tags': tags}

def archives(request):
    archives = Archive.objects.filter(article__status='PUBLISHED').distinct()
    return {'archives': archives}

def wiki_index(request):
    return {'wiki_index': settings.WIKI_INDEX}
