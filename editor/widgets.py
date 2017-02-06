#/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    edior.widgets
    ~~~~~~~~~~~~~~

    widgets for markdown editor powered by
    https://github.com/pandao/editor.md

    :copyright: (c) 2016 by zifeiyu.
    :license: MIT, see LICENSE for more details.
"""
import os
from django import forms
from django.contrib.admin.widgets import AdminTextareaWidget
from django.utils.safestring import mark_safe
from django.template import Context, loader


class EditorWidget(forms.Textarea):

    def __init__(self, attrs=None):
        super(EditorWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        default_widget = super(EditorWidget, self).render(name, value, attrs)
        ctx = {
            'textarea': default_widget
        }
        INIT_TEMPLATE = loader.get_template('editor/editor.html')
        html =  INIT_TEMPLATE.render(Context(ctx))
        return mark_safe(html)


class AdminEditorWidget(EditorWidget, AdminTextareaWidget):
    pass
