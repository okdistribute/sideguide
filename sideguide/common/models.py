from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    # can administer the organization (add destinations, members)
    owners = models.ManyToManyField(User, related_name="own+") 
    # can only add stops, not administer
    members = models.ManyToManyField(User, related_name="mem+") 

class Collection(models.Model):
    name = models.CharField(max_length=45)
    caption = models.CharField(max_length=255)
    description = models.TextField()
    featured = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) 
    org = models.ForeignKey(Organization)
    created_by = models.ForeignKey(User)
    image = models.CharField(max_length=45)

    poly = models.PolygonField()
    objects = models.GeoManager()

class Stop(models.Model):
    name = models.CharField(max_length=45)
    caption = models.CharField(max_length=255)
    description = models.TextField()
    featured = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) 
    coperanda = models.ManyToManyField('self')
    created_by = models.ForeignKey(User)
    number = models.IntegerField(null=True)
    image = models.CharField(max_length=45)
    audio = models.CharField(max_length=45)
    collection = models.ForeignKey(Collection, null=True) 

    point = models.PointField()
    objects = models.GeoManager()

class Tour(models.Model):
    name = models.CharField(max_length=255)

    points = models.MultiPointField()
    objects = models.GeoManager()

