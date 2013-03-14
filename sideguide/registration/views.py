from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from sideguide.registration.models import RegistrationForm, ActivationProfile

def register(request, template_name='registration/register.html',  post_change_redirect='complete'):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect(post_change_redirect)
    else:
        form = RegistrationForm()
    
    return render(request,template_name,
        { 'form': form },
        context_instance=RequestContext(request))

@login_required
def profile(request):
    return render(request,'registration/profile.html')

def activate(request, activation_key,
    template_name='registration/activate.html'):
    activation_key = activation_key.lower()
    if ActivationProfile.activate_user(activation_key):
        return render(request,'registration/activation_successful.html')
    else:
        return render(request,'registration/error.html')
