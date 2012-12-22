from django.db.models import Q
from django.http import HttpResponse
from django.utils import simplejson as json
from django.core import serializers
import datetime
from django.utils.dateparse import parse_datetime
from django.shortcuts import render_to_response
from art.models import Institution

def getInstitutions(request):
    response_status = 20
    inst_id = request.GET.get('id')
    name = request.GET.get('name')
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    address = request.GET.get('address')
    city = request.GET.get('city')
    state  = request.GET.get('state')
    if inst_id or name or (lat and lon) or address or city or state:
        qset = Q()
        if inst_id:
            qset &= Q(id__exact=inst_id)
        if name:
            qset &= Q(name__contains=name)
        if lat:
            qset &= Q(lat__exact=lat)
            qset &= Q(lon__exact=lon)
        if address:
            qset &= Q(address__icontains=address)
        if city:
            qset &= Q(city__icontains=city)
        if state:
            qset &= Q(state__iexact=state)
        insts = Institution.objects.filter(qset)
        response = []
        for inst in insts:
            response.append({
                    'id'             : inst.id,
                    'name'           : inst.name,
                    'lat'            : inst.lat,
                    'lon'            : inst.lon,
                    'address'        : inst.address,
                    'city'           : inst.city,
                    'state'          : inst.state
                    })
    else:
        response = {
            'problem' : 'No parameters specified',
            'details' : ''
            }
        response_status = 400
    return HttpResponse(json.dumps(response), mimetype="application/json", status=response_status)

def getInstitution(request):
    response_status = 200
    inst_id = request.GET.get('id')
    if inst_id:
        qset = Q(id__exact=inst_id)
        inst = Institution.objects.filter(qset)
        if not inst:
            reponse = []
        else:
            response = {
                'id'             : inst[0].id,
                'name'           : inst[0].name,
                'lat'            : inst[0].lat,
                'lon'            : inst[0].lon,
                'address'        : inst[0].address,
                'city'           : inst[0].city,
                'state'          : inst[0].state
                }
    else:
        response = {
            'problem' : 'No id specified',
            'details' : ''
            }
        response_status = 400
    return HttpResponse(json.dumps(response), mimetype="application/json", status=response_status)

