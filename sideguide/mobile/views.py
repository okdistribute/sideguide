from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from common.models import Organization, Collection, Stop

def view(request, orgname=None, coll_id=None, item_id=None, 
            template_name="browse/user.html"):
    """main method for mobile browse view"""
    if coll_id and request.GET.get("view") == "map":
        template_name = "mobile/collection_map.html"

    c = {}
    if not orgname:
        return HttpResponseRedirect("/")

    if orgname:
        c["org"] = Organization.objects.get(name__iexact=orgname)
        c["colls"] = Collection.objects.filter(org=c["org"])
    if coll_id:
        coll = Collection.objects.get(id=coll_id)
        c["coll"] = coll
        c["items"] = Stop.objects.filter(collection=coll)
    if item_id:
        c["item"] = Stop.objects.get(id=item_id)

    return render_to_response(template_name, c)

def index(request, template_name="mobile/index.html"):
    return render_to_response(template_name)
