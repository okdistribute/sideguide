from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    street_line1 = models.CharField(max_length=100, blank=True)
    street_line2 = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)

class Organizations(models.Model):
    name = models.CharField(max_length=255, unique=True)
    # can administer the organization (add destinations, members)
    owners = models.ManyToManyField(User, related_name="own+") 
    # can only add stops, not administer
    members = models.ManyToManyField(User, related_name="mem+") 
    destinations = models.ManyToManyField('Destination')

class Destinations(models.Model):
    name = models.CharField(max_length=255, unique=True)
    org = models.ForeignKey(Organization)
    created_by = models.ForeignKey('self')
    address = models.ForeignKey(Address)
    poly = models.PolygonField()
    objects = models.GeoManager()

class Stops(models.Model):
    name = models.CharField(max_length=45)
    caption = models.CharField(max_length=255)
    description = models.TextField()
    featured = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) 
    coperanda = models.ManyToManyField('self')
    username = models.CharField(max_length=255)
    number = models.IntegerField(null=True)
    point = models.PointField()
    objects = models.GeoManager()
    image = models.CharField(max_length=45)
    audio = models.CharField(max_length=45)
    destination = models.ForeignKey(Destination, blank=True)

class Tours(models.Model):
    name = models.CharField(max_length=255)
    points = models.MultiPointField()
    objects = models.GeoManager()



