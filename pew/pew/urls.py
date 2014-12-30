from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pew.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^markdown/', include( 'django_markdown.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
