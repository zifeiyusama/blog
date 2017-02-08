#/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    blog.widgets
    ~~~~~~~~~~~~~~

    custom widgets used in blog
    https://github.com/pandao/editor.md

    :copyright: (c) 2016 by zifeiyu.
    :license: MIT, see LICENSE for more details.
"""
from django import forms
from django.template import Context, loader
from django.utils.safestring import mark_safe
from django.utils.html import format_html, html_safe
from django.conf import settings
import os


class TagsInputWidget(forms.SelectMultiple):

    def render(self, name, value, attrs=None):
        default_widget = super(TagsInputWidget, self).render(name, value, attrs)
        ctx = {
            'tagsinput': default_widget
        }
        if 'id' in attrs:
            ctx['id'] = attrs['id']
        init_template = loader.get_template('blog/tagsinput.html')
        html = init_template.render(Context(ctx))
        return mark_safe(html)
