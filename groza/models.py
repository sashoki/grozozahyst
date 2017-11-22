# -*- coding: utf-8 -*-

from __future__ import unicode_literals
#from django.contrib.auth.models import User
from django.db import models
#from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
import mptt
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Category(MPTTModel):
    class Meta():
        db_table = 'category'
        verbose_name_plural = 'Категорії'
        verbose_name = 'Категорія'
        ordering = ('tree_id', 'level')

    name = models.CharField(max_length=150, verbose_name = 'Категорія')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=u'Батьківський клас')

    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

mptt.register(Category, order_insertion_by=['name'])


class Portfolio(models.Model):
    class Meta():
        ordering = ['-port_data']
        db_table = 'Portfolio'
        verbose_name_plural = 'Портфоліо'
        verbose_name = 'Портфоліо'

    port_title = models.CharField(max_length=200, verbose_name=u'Назва обєкту')
    port_img = models.ImageField(upload_to="portfolio/", verbose_name='Зображення')
    port_text = RichTextField(verbose_name=u'Опис обєкту')
    port_video = EmbedVideoField(null=True, blank=True, verbose_name=u'Відео')
    port_data = models.DateTimeField(verbose_name=u'Дата закінчення робіт')
    port_client = models.CharField(max_length=200, verbose_name=u'Імя клієнта')
    category = TreeForeignKey(Category, blank=True, null=True, related_name='cat', verbose_name=u'Категорія робіт')

    def __unicode__(self):
        return self.port_title

    def __str__(self):
        return self.port_title

    def bit(self):
        if self.port_img:
            return u'<img src="%s" width="70"/>' % self.port_img.url
        else:
            return '(none)'

    bit.short_description = u'Зображення'
    bit.allow_tags = True