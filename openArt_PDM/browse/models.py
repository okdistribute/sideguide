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
    user = EmbeddedModelField('User')
    tags = ListField(EmbeddedModelField('Tag'))

class Item(models.Model):
    name = models.CharField(max_length=45)
    caption = models.CharField(max_length=255)
    description = models.TextField()
    featured = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) 
    collection_id = models.IntegerField() 
    coperanda = ListField(EmbeddedModelField('Item'))
    tags = ListField(EmbeddedModelField('Tag'))

class Tag(models.Model):
    text = models.CharField(unique=True, max_length=24)
    







    
    

