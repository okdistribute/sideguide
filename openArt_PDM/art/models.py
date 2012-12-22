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
    user = EmbeddedModelField(User)
    items = ListField(EmbeddedModelField('Item'))

    def json(self):
        return {
                'id'             : self.id,
                'name'           : self.name,
                'caption'        : self.caption,
                'description'    : self.description,
                'featured'       : self.featured,
                'created_at'     : str(self.created_at),
                'last_modified'  : str(self.last_modified),
                'user'           : str(self.user),
                'items'          : [i.json() for i in self.items],
                }

class Item(models.Model):
    name = models.CharField(max_length=45)
    caption = models.CharField(max_length=255)
    description = models.TextField()
    featured = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) 
    coperanda = ListField(EmbeddedModelField('Item'))
    user = EmbeddedModelField(User)
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
                'user'           : str(self.user),
                'image'          : self.image,
                'audio'          : self.audio,
                }

    
