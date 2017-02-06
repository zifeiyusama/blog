#/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    blog.views
    ~~~~~~~~~~~~~~

    views functions for blog

    :copyright: (c) 2016 by zifeiyu.
    :license: MIT, see LICENSE for more details.
'''
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Article, Column, Archive, Tag

from django.core.paginator import Paginator, InvalidPage


def articles(request, archive=None, column=None, tag=None):
    articles = Article.objects.filter(status='PUBLISHED')
    if archive is not None:
        articles = articles.filter(archive__abbreviation=archive)
    if column is not None:
        articles = articles.filter(column__id=column)
    if tag is not None:
        articles = articles.filter(tags__label=tag)
    articles = articles.order_by('-published_date')
    # pagination
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except InvalidPage:
        articles = paginator.page(1)
    return render(request, 'blog/index.html', {'articles': articles})

def article(request, article):
    #TODO:修改为专一的URL
    context = {}
    try:
        article = Article.objects.filter(status='PUBLISHED').get(pk=article)
        context['article'] = article
    except ObjectDoesNotExist:
        raise Http404('article not found')
    return render(request, 'blog/article.html', context)

def about(request):
    return HttpResponse('this is the about page')

def wiki(request):
    return HttpResponse('this is the wiki page')
