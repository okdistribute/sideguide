from django.contrib.auth.models import User
from django.db import models
from djangotoolbox.fields import EmbeddedModelField

class Collection(models.Model):
    name = models.CharField(max_length=45)
    caption = models.CharField(max_length=255)
    description = models.TextField()
    featured = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) 
    user = models.EmbeddedModelField('User')
    tags = models.ListField(models.EmbeddedModelField('Tag'))

class Item(models.Model):
    name = models.CharField(max_length=45)
    caption = models.CharField(max_length=255)
    description = models.TextField()
    featured = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) 
    collection_id = models.IntegerField() 
    coperanda = models.ListField(models.EmbeddedModelField('Item'))
    tags = models.ListField(models.EmbeddedModelField('Tag'))

class Tag(models.Model):
    text = models.CharField(unique=True, max_length=24)
    







    
    

