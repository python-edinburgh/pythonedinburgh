from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^$', 'main.views.home', name='home'),

    url(r'^events/',    include('events.urls')),
    url(r'^markdown/',  include('django_markdown.urls')),
    url(r'^admin/',     include(admin.site.urls)),
)
