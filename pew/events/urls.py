from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import EventDetails

urlpatterns = patterns('',
    url(r'^(?P<slug>[a-z_-]+)$', EventDetails.as_view(), name='event-details'),
)
