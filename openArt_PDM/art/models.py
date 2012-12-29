from django.contrib.auth.models import User
from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField
from django.utils import simplejson as json

class Collection(models.Model):
    name = models.CharField(max_length=45)
    caption = models.CharField(max_length=255)
    description = models.TextField()
    featured = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) 
    username = models.CharField(max_length=255)
    items = ListField(EmbeddedModelField('Item'))
    image = models.CharField(max_length=45)

    def json(self):
        return {
                'id'             : self.id,
                'name'           : self.name,
                'caption'        : self.caption,
                'description'    : self.description,
                'featured'       : self.featured,
                'created_at'     : str(self.created_at),
                'last_modified'  : str(self.last_modified),
                'username'       : str(self.username),
                'items'          : [i.json() for i in self.items],
                'image'          : self.image,
                }

class Item(models.Model):
    name = models.CharField(max_length=45)
    caption = models.CharField(max_length=255)
    description = models.TextField()
    featured = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) 
    coperanda = ListField(EmbeddedModelField('Item'))
    username = models.CharField(max_length=255)
    #XXX: change these following from static references to GridFS before going to alpha 
    image = models.CharField(max_length=45)
    audio = models.CharField(max_length=45)

    def json(self):
        return {
                'id'             : self.id,
                'name'           : self.name,
                'caption'        : self.caption,
                'description'    : self.description,
                'featured'       : self.featured,
                'created_at'     : str(self.created_at),
                'last_modified'  : str(self.last_modified),
                'coperanda'      : [i.json() for i in self.coperanda],
                'username'       : str(self.username),
                'image'          : self.image,
                'audio'          : self.audio,
                }

    
