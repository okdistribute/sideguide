from django.shortcuts import render_to_response

def index(request):
    c = {}
    return render_to_response("browse/explore.html", c)

def dest(request):
    """/browse/destinationname
    :returns a view of that destination"""

    c = {}
    return render_to_response("browse/")