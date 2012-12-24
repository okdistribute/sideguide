from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    url(r'^(?P<username>\w+)$', 'mobile.views.view',
        {"template_name": "mobile/user.html"}),
    url(r'^(?P<username>\w+)/(?P<coll_id>\w+)$', 'mobile.views.view',
        {"template_name": "mobile/collection.html"}),
    url(r'^(?P<username>\w+)/(?P<coll_id>\w+)/(?P<item_id>\w+)$','mobile.views.view', 
        {"template_name": "mobile/item.html"}),
)
