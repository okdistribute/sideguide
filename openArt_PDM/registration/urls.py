from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
	url(r'^activate/(?P<activation_key>\w+)/$', 'registration.views.activate'),
	url(r'^login/$', auth_views.login, 
		{'template_name': 'registration/login.html'}),
	url(r'^logout/$', auth_views.logout,
		{'template_name': 'registration/logged_out.html'}),
	url(r'^password/change/$', auth_views.password_change,
		{'template_name': 'registration/password_change_form.html', 
		'post_change_redirect': 'done'}),
	url(r'^password/change/done/$', auth_views.password_change_done,
	 	{'template_name': 'registration/password_change_done.html'}),





	url(r'^password/reset/$', auth_views.password_reset,
		{'template_name': 'registration/password_reset.html'}),
	url(r'^password/reset/done/$', auth_views.password_reset_done,
		{'template_name': 'registration/password_reset_done.html',
		'email_template_name': 'registration/password_reset_email.html'}),
    url(r'^register/$', 'registration.views.register'),
    url(r'^register/complete/$', direct_to_template, 
    	{'template': 'registration/registration_complete.html'}),  
    url(r'^profile/$', 'registration.views.profile'),
)
