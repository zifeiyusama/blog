#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    blog.templatetags.blog_extras
    ~~~~~~~~~~~~~~

    add momentjs filter

    :copyright: (c) 2016 by zifeiyu.
    :license: MIT, see LICENSE_FILE for more details.
"""
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def formatdate(value, format):
    return mark_safe("<script>document.write(moment(\"%s\").format(\"%s\"));</script>" \
    % (value.strftime("%Y-%m-%dT%H:%M:%S Z"), format))
