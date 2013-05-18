from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    url(r'^$', 'mobile.views.index',
        {"template_name": "mobile/index.html"}),
    url(r'^ajax/(?P<orgname>\w+)$', 'mobile.views.view',
        {"template_name": "mobile/user.html"}),
    url(r'^ajax/(?P<orgname>\w+)/(?P<coll_id>\w+)$', 'mobile.views.view',
        {"template_name": "mobile/collection.html"}),
    url(r'^ajax/(?P<orgname>\w+)/(?P<coll_id>\w+)/(?P<item_id>\w+)$','mobile.views.view', 
        {"template_name": "mobile/item.html"}),
 )
