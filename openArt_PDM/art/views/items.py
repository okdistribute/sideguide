from django.db.models import Q
from django.http import HttpResponse
from django.utils import simplejson as json
from django.core import serializers
from django.shortcuts import render_to_response
from art.models import Item
from dateutil.parser import parse as parse_datetime
import datetime

def getItems(request):
    response_status = 200
    user_id = request.GET.get('user_id')
    featured = request.GET.get('featured')
    name = request.GET.get('name')
    created_at_str = request.GET.get('created_at')
    if user_id or featured or name or created_at_str:
        qset = Q()
        if user_id:
            qset &= Q(user__id__exact=user_id)
        if featured:
            qset &= Q(featured__iexact=featured)
        if name:
            qset &= Q(name__icontains=name)
        if created_at_str:
            created_at = parse_datetime(created_at_str)
            qset &= Q(created_at__year=created_at.year)
            qset &= Q(created_at__month=created_at.month)
            qset &= Q(created_at__day=created_at.day)
        items = Item.objects.filter(qset)
        response = []
        for item in items:
            qset = Q(item__id=item.id)
            response.append(item.json())
    else:
        response = {
            'problem' : 'No parameters specified',
            'details' : ''
            }
        response_status = 400
    return HttpResponse(json.dumps(response), mimetype="application/json", status=response_status)

def getItem(request):
    response_status = 200
    item_id = request.GET.get('id')
    if item_id:
        qset = Q(id__exact=item_id)
        items = Item.objects.filter(qset).select_related()
        if not items:
            response = []
        else:
            item = items[0]
            qset = Q(item__id=item.id)
            response = item.json() 
    else:
        response = {
            'problem' : 'No id specified',
            'details' : ''
            }
        response_status = 400
    return HttpResponse(json.dumps(response), mimetype="application/json", status=response_status)
