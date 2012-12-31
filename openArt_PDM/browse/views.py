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
from art.models import Item, Collection

def view(request, username=None, coll_id=None, item_id=None, 
        template_name="browse/user.html"):
    """main method for mobile browse view"""
    if coll_id and request.GET.get("view") == "map":
        template_name = "mobile/collection_map.html"

    c = {}
    if not username:
        return HttpResponseRedirect("/")

    if username:
        c["user"] = User.objects.get(username__iexact=username)
        c["colls"] = Collection.objects.filter(username__iexact=username)
    if coll_id:
        coll = Collection.objects.get(id=coll_id)
        c["coll"] = coll
        c["items"] = [i.json() for i in coll.items]
    if item_id:
        c["item"] = Item.objects.get(id=item_id)

    return render_to_response(template_name, c)
