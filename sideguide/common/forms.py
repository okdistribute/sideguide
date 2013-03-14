from django.forms import ModelForm
from models import *

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization

class CollForm(ModelForm):
    class Meta:
        model = Collection