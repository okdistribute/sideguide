from django.conf.urls import patterns, url

urlpatterns = patterns('browse.views',
    url(r'^explore$', "explore.index"),
    url(r'^explore/(\w+)/$', 'explore.dest'),

    url(r'^curate$', 'curate.index'),
)
