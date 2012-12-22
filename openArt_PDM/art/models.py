from django.contrib.auth.models import User
from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField

class Collection(models.Model):
    name = models.CharField(max_length=45)
    caption = models.CharField(max_length=255)
    description = models.TextField()
    featured = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) 
    user = EmbeddedModelField(User)

class Item(models.Model):
    name = models.CharField(max_length=45)
    caption = models.CharField(max_length=255)
    description = models.TextField()
    featured = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) 
    collection = ListField(EmbeddedModelField(Collection))
    coperanda = ListField(EmbeddedModelField('Item'))
    #XXX: change these following from static references to GridFS before going to alpha 
    image = models.CharField(max_length=45)
    audio = models.CharField(max_length=45)

    
