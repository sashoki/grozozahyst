# -*- coding: utf-8 -*-

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from groza.models import Portfolio, Category

# Register your models here.

class PortfolioAdmin(admin.ModelAdmin):
    fields = ['port_title', 'port_img', 'port_text', 'port_video', 'port_data', 'port_client', 'category']
    list_display = ('port_title', 'port_data', 'port_img', 'category')
    list_filter = ['category']
    search_fields = ['port_title']

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'parent']

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Category, CategoryAdmin)