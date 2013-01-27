from django.contrib.auth.models import User
from django.db import models
from django.utils import simplejson as json

class Map(models.Model):
    name = models.CharField(max_length=20)
    index = models.IntegerField(default=0)
    #XXX: the following should be a GridFS pointer later
    image = models.CharField(max_length=45)
 #   items = ListField(EmbeddedModelField('Item'))

class Location(models.Model):
    name = models.CharField(max_length=45)
    street_line1 = models.CharField(max_length=100, blank=True)
    street_line2 = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=255)
#    maps = models.ForiegnKey('Map'))
 #   collections = ListField(EmbeddedModelField('Collection'))

class Collection(models.Model):
    name = models.CharField(max_length=45)
    caption = models.CharField(max_length=255)
    description = models.TextField()
    featured = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) 
    username = models.CharField(max_length=255)
 #   items = ListField(EmbeddedModelField('Item'))
    image = models.CharField(max_length=45)

class Item(models.Model):
    name = models.CharField(max_length=45)
    caption = models.CharField(max_length=255)
    description = models.TextField()
    featured = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) 
    #coperanda = ListField(EmbeddedModelField('Item'))
    username = models.CharField(max_length=255)
    number = models.IntegerField(null=True)
    x = models.IntegerField(null=True)
    y = models.IntegerField(null=True)
    #XXX: change these following from static references to GridFS before going to alpha 
    image = models.CharField(max_length=45)
    audio = models.CharField(max_length=45)

