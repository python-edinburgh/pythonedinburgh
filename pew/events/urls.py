from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import EventDetails

urlpatterns = patterns('',
    url(
        r'^(?P<year>\d+)/(?P<month>\d+)/(?P<slug>[a-z0-9_-]+)$',
        EventDetails.as_view(), name='event-details'),
)
