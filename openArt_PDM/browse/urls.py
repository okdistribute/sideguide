from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    url(r'^(?P<username>\w+)$', 'browse.views.user'),
    url(r'^(?P<username>\w+)/(?P<collection>\w+)$', 'browse.views.collection'),
    url(r'^(?P<username>\w+)/(?P<collection>\w+)/(?P<item>\w+)$', 'browse.views.item')
)
