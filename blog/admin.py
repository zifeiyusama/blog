#/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    blog.admin
    ~~~~~~~~~~~~~~

    register admin for models

    :copyright: (c) 2016 by zifeiyu.
    :license: MIT, see LICENSE for more details.
"""
from django.contrib import admin
from .models import Column, Article, Archive, Tag
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.db import models

from django.utils import timezone

from editor.widgets import AdminEditorWidget
from editor.models import EditorField

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_date',
        'modified_date',
        'published_date',
        'deleted_date',
        'archive'
    )
    fieldsets = (
        (
        None, {
            'fields': (
                'title',
                'status',
                ('archive', 'column', 'tags'),
                'abstract_content',
                'content',
            )
        }),
        (
            '更多信息',
            {
                'fields': (
                    'created_date',
                    'modified_date',
                    'published_date',
                    'deleted_date'
                ),
            }
        )
    )
    list_display = ('title', 'column', 'archive', 'status', 'created_date',
                    'published_date')
    ordering = ['created_date', 'published_date']
    list_filter = ('column', 'archive', 'status')
    formfield_overrides = {EditorField: {'widget': AdminEditorWidget}}
    list_per_page = 15
    save_as = True
    save_as_continue = False
    save_on_top = True
    search_fields = ['title']
    filter_horizontal = ('tags',)
    actions = ['make_published']

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='PUBLISHED', published_date = timezone.now())
        message_bit = "%s 篇文章发布成功" % rows_updated
        self.message_user(request, message_bit)
    make_published.short_description = "发布"


class ArticleInline(admin.TabularInline):
    model = Article
    fields = ('title', 'column', 'status', 'created_date', 'published_date')
    readonly_fields = ('title', 'column', 'status', 'created_date', 'published_date')
    extra = 0
    can_delete = False
    verbose_name = '文章'
    verbose_name_plural = '文章'
    show_change_link = True

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('label', 'article_count', 'created_date')
    ordering = ['created_date']
    actions = None
    fieldsets = (
        (
            '基本信息', {
                'fields': (
                    ('label', 'article_count'),
                    'created_date'
                )
            },
        ),
    )
    readonly_fields = ('label', 'created_date', 'article_count')
    inlines = [
        ArticleInline
    ]

    def has_add_permission(self, request):
        return False


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('label', 'article_count', 'created_date', 'modified_date')
    ordering = ('modified_date',)
    fieldsets = (
        (
            '基本信息', {
                'fields': (
                    'label',
                    'article_count',
                    ('created_date', 'modified_date')
                )
            }
        ),
    )
    readonly_fields = ('modified_date', 'created_date', 'article_count')
    inlines = [
        ArticleInline
    ]

    def save_model(self, request, obj, form, change):
        try:
            column = Column.objects.get(label=obj.label)

            self.message_user(request, '栏目已经存在', level=messages.WARNING)
            return
        except ObjectDoesNotExist:
            super(ArticleAdmin, self).save_model(request, obj, form, change)


class ArticleM2MInline(ArticleInline):
    model = Article.tags.through
    fields = ('article',)
    readonly_fields = ('article',)
    show_change_link = False

@admin.register(Tag)
class TagAdmin(ColumnAdmin):
    inlines = [
        ArticleM2MInline
    ]
