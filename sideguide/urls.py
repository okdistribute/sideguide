from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from tastypie.api import Api
from common.api import * 
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(CollectionsResource())
v1_api.register(StopsResource())


urlpatterns = patterns('',
    # url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^accounts/', include('registration.urls')),
    url(r'^policies/services/$', direct_to_template,
        {'template': 'TermsOfService.html'}),
    url(r'^policies/privacy/$', direct_to_template,
        {'template': 'PrivacyPolicy.html'}),

     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),

     url(r'^m/', include('mobile.urls')),
     url(r'^$', include('browse.urls')),
     url(r'^api/', include(v1_api.urls)),
)
