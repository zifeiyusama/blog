#/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    editor.admin
    ~~~~~~~~~~~~~~

    editor support in admin site

    :copyright: (c) 2016 by zifeiyu.
    :license: MIT, see LICENSE for more details.
"""
from django.contrib import admin

from .widgets import AdminEditorWidget
from .models import EditorField

class EditorModelAdmin(admin.ModelAdmin):
    formfield_overrides = {EditorField: {'widget': AdminEditorWidget}}
