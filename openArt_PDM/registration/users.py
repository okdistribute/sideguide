from django.db.models import Q
from django.http import HttpResponse
from django.utils import simplejson as json
from django.core import serializers
import datetime
from django.utils.dateparse import parse_datetime
from django.shortcuts import render_to_response
from art.models import User
from common.utils import *

def getUsers(request):
    response_status = 200
    sn = request.GET.get('screen_name')
    mail = request.GET.get('email')
    if sn or mail:
        users = User.objects(__raw__={'$or':[{'_id':sn}, {'email':mail}]})
        response = []
        for user in users:
            print user
            response.append({
                    "screen_name"  : user.screen_name,
                    "email"        : user.email,
                    "full_name"    : user.full_name,
                    "created_at" : str(user.created_at)
                    })
    else:
        return response400('No user identifiers specified', '')
    return HttpResponse(json.dumps(response), mimetype="application/json", status=response_status)

def getUser(request):
    response_status = 200
    screen_name = request.GET.get('screen_name')

    if screen_name:
        user = User.objects(screen_name__exact=screen_name)
        if not user:
            response = []
        else:
            response = {
                "screen_name"  : user[0].screen_name,
                "email"        : user[0].email,
                "full_name"    : user[0].full_name,
                "created_at" : str(user[0].created_at)
                }
    else:
        return response400('No screen_name specified', '')
    return HttpResponse(json.dumps(response), mimetype="application/json", status=response_status)

def createUser(request):
    if not authenticated(request):
        return response401()
    sn = request.POST.get('screen_name')
    name = request.POST.get('full_name')
    mail = request.POST.get('email')
    password = request.POST.get('password')
    if sn and mail and password:
        users = User.objects(__raw__={'$or':[{'screen_name':sn}, {'email':mail}]})
        if users:
            return response400('screen_name or email already exist', sn + ' ' + mail)
        else:
            import random
            algo = 'sha1'
            slt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
            hsh = get_hexdigest(algo, slt, password)
            user = User(screen_name=sn, full_name=name, email=mail, password=hsh, salt=slt)
            user.save()
            response = {
                "screen_name"  : user.screen_name,
                "email"        : user.email,
                "full_name"    : user.full_name,
                "created_at" : str(user.created_at)
                }
            response_status = 201
    else:
        return response400('screen_name, email and password required', '')
    return HttpResponse(json.dumps(response), mimetype="application/json", status=response_status)

def updateUser(request):
    if not authenticated(request):
        return response401()
    sn = request.POST.get('screen_name')
    name = request.POST.get('full_name')
    password = request.POST.get('password')
    if sn:
        user = User.objects(screen_name__exact=sn)
        if not user:
            return response400('user does not exist', sn)
        if name:
            user[0].full_name = name
        if password:
            algo = 'sha1'
            slt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
            hsh = get_hexdigest(algo, slt, password)
            user[0].salt = slt
            user[0].password = hsh
        user[0].save()
        response = {
            "screen_name"  : user[0].screen_name,
            "email"        : user[0].email,
            "full_name"    : user[0].full_name,
            "created_at" : str(user[0].created_at)
            }
        response_status = 201
    else:
        return response400('screen_name required', '')
    return HttpResponse(json.dumps(response), mimetype="application/json", status=response_status)

def deleteUser(request):
    if not authenticated(request):
        return response401()
    sn = request.GET.get('screen_name')
    if sn:
        user = User.objects(screen_name__exact=sn)
        if user:
            user[0].delete()
            return HttpResponse('[]', mimetype="application/json", status=200)
        else:
            return response400('user does not exist', sn)
    return response400('screen_name required', '')

