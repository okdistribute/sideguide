from django.shortcuts import render

def index(request):
    c = {}
    return render(request, "browse/explore.html", c)

def dest(request):
    """/browse/destinationname
    :returns a view of that destination"""

    c = {}
    return render(request, "browse/", c)