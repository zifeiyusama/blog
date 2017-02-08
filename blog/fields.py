#/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    blog.fields
    ~~~~~~~~~~~~~~

    custom fields used in blog
    https://github.com/pandao/editor.md

    :copyright: (c) 2016 by zifeiyu.
    :license: MIT, see LICENSE for more details.
"""


from django import forms
from .widgets import TagsInputWidget


class TagsInputFormField(forms.ModelMultipleChoiceField):
    def __init__(self, *args, **kwargs):
        super(TagsInputFormField, self).__init__(*args, **kwargs)
        self.widget = TagsInputWidget()

    def _check_values(self, value):
        """
        Given a list of possible PK values, returns a QuerySet of the
        corresponding objects. Raises a ValidationError if a given value is
        invalid (not a valid PK, not in the queryset, etc.)
        """
        key = self.to_field_name or 'pk'
        # deduplicate given values to avoid creating many querysets or
        # requiring the database backend deduplicate efficiently.
        try:
            value = frozenset(value)
        except TypeError:
            # list of lists isn't hashable, for example
            raise ValidationError(
                self.error_messages['list'],
                code='list',
            )
        qs = self.queryset.filter(**{'%s__in' % key: value})
        pks = set(getattr(o, key) for o in qs)
        for val in value:
            if val not in pks:
                self.queryset.create(label=val)
        qs = self.queryset.filter(**{'%s__in' % key: value})
        return qs
