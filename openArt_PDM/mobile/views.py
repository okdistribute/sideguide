from django.shortcuts import render_to_response

def index(request, template_name="mobile/index.html"):
    return render_to_response(template_name)
