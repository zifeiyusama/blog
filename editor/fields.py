#/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    edior.fields
    ~~~~~~~~~~~~~~

    form field using editor widget

    :copyright: (c) 2016 by zifeiyu.
    :license: MIT, see LICENSE for more details.
"""
from django import forms
from .widgets import EditorWidget


class EditorFormField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super(EditorFormField, self).__init__(*args, **kwargs)
        self.widget = EditorWidget()
