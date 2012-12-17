from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, forms
from django.contrib.auth.decorators import login_required
from django.template import Context, Template
from django.utils import simplejson

from registration.models import RegistrationForm, ActivationProfile, Address

def register(request, 
    template_name='registration/register.html',
    post_change_redirect='complete'):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect(post_change_redirect)
    else:
        form = RegistrationForm()
    
    return render_to_response(template_name, 
        { 'form': form },
        context_instance=RequestContext(request))

@login_required
def profile(request):
    address = request.user.get_profile().address
    return render_to_response('registration/profile.html', 
        { 'address' : address },
        context_instance=RequestContext(request))

def activate(request, activation_key,
    template_name='registration/activate.html'):
    activation_key = activation_key.lower()
    if ActivationProfile.activate_user(activation_key):
        return render_to_response('registration/activation_successful.html')
    else:
        return render_to_response('registration/error.html')
