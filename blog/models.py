#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    blog.models
    ~~~~~~~~~~~~~~

    Model definition for blog

    :copyright: (c) 2016 by zifeiyu.
    :license: MIT, see LICENSE_FILE for more details.
"""

import uuid
from django.utils import timezone

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from editor.models import EditorField
from .fields import TagsInputFormField


class BaseModel(models.Model):

    id = models.UUIDField(primary_key=True, editable=False)
    created_date = models.DateTimeField(verbose_name=_('created date'), auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name=_('modified date'), auto_now=True)

    class Meta:
        abstract = True

    def get_uuid(self):
        namespace = uuid.uuid1()
        result = uuid.uuid5(namespace, name=self.__class__.__name__).hex
        return result

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.get_uuid()
        super(BaseModel, self).save(*args, **kwargs)


class ParentBase(BaseModel):
    label = models.CharField(verbose_name=_('label'), max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.label

    def article_count(self):
        return self.articles.count()

    article_count.short_description = '文章数量'



class Tag(ParentBase):

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class Archive(ParentBase):
    abbreviation = models.CharField(verbose_name=_('abbreviation'), max_length=6, blank=True, null=True)

    @classmethod
    def generate_label(cls):
        return timezone.now().strftime('%Y年%m月'), \
               timezone.now().strftime('%Y%m')

    def save(self, *args, **kwargs):
        self.label, self.abbreviation = Archive.generate_label()
        super(Archive, self).save(*args,**kwargs)

    class Meta:
        verbose_name = _('Archive')
        verbose_name_plural = _('Archives')


class Column(ParentBase):

    class Meta:
        verbose_name = _('Column')
        verbose_name_plural = _('Columns')


class TagsInputField(models.ManyToManyField):
    def formfield(self, **kwargs):
        defaults = {
            'form_class': TagsInputFormField,
            'to_field_name': 'label',
        }
        defaults.update(kwargs)
        return super(TagsInputField, self).formfield(**defaults)

class Article(BaseModel):
    PUBLISHED = ('PUBLISHED', '已发布')
    DRAFT = ('DRAFT', '草稿')
    status_choices = (DRAFT, PUBLISHED)
    title = models.CharField(verbose_name=_('title'), max_length=50)
    # content = models.TextField()
    content = EditorField(verbose_name=_('content'))
    abstract_content = models.TextField(verbose_name=_('abstract content'))
    status = models.CharField(verbose_name=_('status'), max_length=10,
                              choices=status_choices, default=DRAFT)
    column = models.ForeignKey(Column, verbose_name=_('column'),
                               related_name='articles',
                               related_query_name='article',
                               blank=True, null=True)
    archive = models.ForeignKey(Archive, verbose_name=_('archive'),
                                related_name='articles',
                                related_query_name='article')
    tags = TagsInputField(Tag, verbose_name=_('tags'),
                                  related_name='articles',
                                  related_query_name='article',
                                  blank=True)
    published_date = models.DateTimeField(verbose_name=_('published date'),
                                          blank=True, null=True)
    deleted_date = models.DateTimeField(verbose_name=_('deleted date'),
                                        blank=True, null=True)

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def save(self, *args, **kwargs):
        if not hasattr(self, 'archive'):
            try:
                label, abbreviation = Archive.generate_label()
                archive = Archive.objects.get(label=label, abbreviation=abbreviation)
                self.archive = archive
            except ObjectDoesNotExist:
                archive = Archive()
                archive.save()
                self.archive = archive
        if self.published_date is None and self.status == 'PUBLISHED':
            self.published_date = timezone.now()
        if self.status == 'DRAFT':
            self.published_date = None
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
