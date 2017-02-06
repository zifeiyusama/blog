#/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    edior.models
    ~~~~~~~~~~~~~~

    model field using editor widget

    :copyright: (c) 2016 by zifeiyu.
    :license: MIT, see LICENSE for more details.
"""
from django.db import models

from .fields import EditorFormField

class EditorField(models.TextField):
    def formfield(self, **kwargs):
        defaults = {'form_class': EditorFormField}
        defaults.update(kwargs)
        return super(EditorField, self).formfield(**defaults)
