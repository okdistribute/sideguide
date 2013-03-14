from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from sideguide.common.forms import CollForm

def index(request):
    """/curate"""
    c = {}
    return render(request, "browse/curate.html", c)

def dest(request):
    """/curate/desintation-name
    :returns a view of that destination for curation"""

    c = {}
    return render(request, "browse/curate.html", c)

@require_http_methods(["POST"])
def create_coll(request):
    """/curate
    creates a collection"""
    form = CollForm(request)
    c = {}
    return render(request, "browse/curate.html", c)