from django.conf.urls import patterns, include, url
from tastypie.api import Api
from django.contrib import admin
from common.api import *
from django.views.generic import RedirectView, TemplateView

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(CollectionsResource())
v1_api.register(StopsResource())

urlpatterns = patterns('',
    # url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^accounts/', include('registration.urls')),
    url(r'^policies/services/$',TemplateView.as_view(template_name='TermsOfService.html')),
    url(r'^policies/privacy/$',TemplateView.as_view(template_name='PrivacyPolicy.html')),

     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),

     url(r'^$', "common.views.splash"),
     url(r'^', include("browse.urls")),
     url(r'^m/', include("mobile.urls")),

    url(r'^api/', include(v1_api.urls)),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/fav.ico')),
    url(r'', include('social_auth.urls')),

)
