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
    inst_id = request.GET.get('institution_id')
    name = request.GET.get('name')
    if coll_id or inst_id or name:
        qset = Q()
        if coll_id:
            qset &= Q(id__exact=coll_id)
        if inst_id:
            qset &= Q(institution__id__exact=inst_id)
        if name:
            qset &= Q(name__iexact=name) 
        colls = Collection.objects.filter(qset).select_related('institution')
        response = []
        for coll in colls:
            response.append({
                    'id'             : coll.id,
                    'institution_id' : coll.institution.id,
                    'name'           : coll.name,
                    'caption'        : coll.caption,
                    'description'    : coll.description
                    })
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
        colls = Collection.objects.filter(qset).select_related('institution')
        if not colls:
            response = []
        else:
            coll = colls[0]
            response = {
                'id'             : coll.id,
                'institution_id' : coll.institution.id,
                'name'           : coll.name,
                'caption'        : coll.caption,
                'description'    : coll.description
                }
    else:
        response = {
            'problem' : 'No id specified',
            'details' : ''
            }
        response_status = 400
    return HttpResponse(json.dumps(response), mimetype="application/json", status=response_status)
