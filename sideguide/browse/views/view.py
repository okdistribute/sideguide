from django.shortcuts import render_to_response

def view(response):
    return render_to_response("hello")