from django.conf.urls import url, include
from django.contrib import admin

from django.contrib import admin
admin.autodiscover()

urlpatterns = [

    url(r'^$', 'groza.views.portfolios', name='portfolios'),
    url(r'^callback/$', 'groza.views.callback', name='callback'),
    url(r'^thanks/$', 'groza.views.callback', name='thanks'),

    ]