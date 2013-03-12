from tastypie.resources import ModelResource
from sideguide.common.models import *

class StopsResource(ModelResource):
    class Meta:
        queryset = Stop.objects.all()
        resource_name = 'stops'

class CollectionsResource(ModelResource):
    class Meta:
        queryset = Collection.objects.all()
        resource_name = 'collections'
