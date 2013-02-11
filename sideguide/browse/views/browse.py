from django.shortcuts import render_to_response

def view(request):
    c = {}
    return render_to_response("browse/view.html", c)
