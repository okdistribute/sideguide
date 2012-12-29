from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# url(r'^$', 'django.contrib.auth.views.login'),
	url(r'^accounts/', include('registration.urls')),
    url(r'^policies/services/$', direct_to_template,
        {'template': 'TermsOfService.html'}),
    url(r'^policies/privacy/$', direct_to_template,
        {'template': 'PrivacyPolicy.html'}),


    # Examples:
    # url(r'^$', 'openArt.views.home', name='home'),
    # url(r'^openArt/', include('openArt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

     url(r'^art/', include('art.urls')),
     url(r'^browse/', include('browse.urls')),
     url(r'^m/', include('mobile.urls')),
)
