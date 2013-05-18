from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    owners = models.ManyToManyField(User, related_name="own+") 
    members = models.ManyToManyField(User, related_name="mem+") 

class Collection(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) 
    org = models.ForeignKey(Organization, null=True)
    created_by = models.ForeignKey(User)
    image = models.CharField(max_length=45)
    objects = models.GeoManager()

class Stop(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) 
    coperanda = models.ManyToManyField('self')
    created_by = models.ForeignKey(User)
    org = models.ForeignKey(Organization, null=True)
    number = models.IntegerField(null=True)
    image = models.CharField(max_length=45)
    audio = models.CharField(max_length=45)
    collection = models.ForeignKey(Collection, null=True)
    point = models.PointField()
    objects = models.GeoManager()

