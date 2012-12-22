from django.db.models import Q
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render_to_response
from art.models import Collection
from django.utils import simplejson as json
from dateutil.parser import parse as parse_datetime
import datetime

def getCollections(request):
    response_status = 200
    coll_id = request.GET.get('id')
    name = request.GET.get('name')
    if coll_id or name:
        qset = Q()
        if coll_id:
            qset &= Q(id__exact=coll_id)
        if name:
            qset &= Q(name__iexact=name) 
        colls = Collection.objects.filter(qset)
        response = []
        for coll in colls:
            response.append(coll.json())
    else:
        response = {
            'problem' : 'No parameters specified',
            'details' : ''
            }
        response_status = 400
    return HttpResponse(json.dumps(response), mimetype="application/json", status=response_status)

def getCollection(request):
    response_status = 200
    coll_id = request.GET.get('id')
    if coll_id:
        qset = Q(id__exact=coll_id)
        colls = Collection.objects.filter(qset)
        if not colls:
            response = []
        else:
            coll = colls[0]
            response = coll.json()
    else:
        response = {
            'problem' : 'No id specified',
            'details' : ''
            }
        response_status = 400
    return HttpResponse(json.dumps(response), mimetype="application/json", status=response_status)
