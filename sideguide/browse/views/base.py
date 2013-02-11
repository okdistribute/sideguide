from django.shortcuts import render_to_response

def splash(request):
    c = {}
    return render_to_response("browse/splash.html", c)
