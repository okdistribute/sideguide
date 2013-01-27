from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, forms
from django.contrib.auth.decorators import login_required
from django.template import Context, Template
from django.utils import simplejson
from django.contrib.auth.models import User
from django.db.models import Q
from common.models import *

def splash(request):
    c = {}
    return render_to_response("browse/splash.html", c)
