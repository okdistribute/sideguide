from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, forms
from django.contrib.auth.decorators import login_required
from django.template import Context, Template
from django.utils import simplejson
from django.contrib.auth.models import User
from art.models import Item, Collection

def user(request, username):
    c = {}
    return render_to_response('browse/user.html', c)


def collection(request, username, collection):
    c = {}
    return render_to_response('browse/collection.html', c)


def item(request, username, collection, item):
    c = {}
    return render_to_response('browse/item.html', c)
