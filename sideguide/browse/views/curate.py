from django.shortcuts import render_to_response

def index(request):
    """/curate"""
    c = {}
    return render_to_response("browse/curate.html", c)

def dest(request):
    """/curate/desintation-name
    :returns a view of that destination for curation"""

    c = {}
    return render_to_response("browse/")