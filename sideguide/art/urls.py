from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    url(r'^items$', 'art.views.items.getItems'),
    url(r'^item$', 'art.views.items.getItem'),
    url(r'^collections$', 'art.views.collections.getCollections'),
    url(r'^collection$', 'art.views.collections.getCollection'),
)
