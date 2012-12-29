from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    url(r'^$', 'mobile.views.index',
        {"template_name": "mobile/index.html"}),
 )
