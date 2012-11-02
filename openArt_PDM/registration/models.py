import sha
import random

from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(
		max_length=75,
		widget=forms.TextInput(attrs={'class': 'required'}),
		label='Email')
	# HERE: implement location as embedded object in mongoDB
	accept_terms_and_privacy = forms.BooleanField(
		widget=forms.CheckboxInput(attrs={'class': 'required'}),
		error_messages={'required': 'Please read and agree to the Terms of Service and Privacy Policy.'})
	def save(self):
		new_user = ActivationProfile.create_inactive_user(
			username=self.cleaned_data['username'],
			email=self.cleaned_data['email'],
			password=self.cleaned_data['password1'])
		new_user.save()
		return new_user

class ActivationProfile(models.Model):
	user = models.CharField(max_length=30)
	activation_key = models.CharField(max_length=40)

	def __unicode__(self):
		return "Activation information for %s" % self.username

	@classmethod
	def create_inactive_user(cls, username, password, email, send_email=False):
		new_user = User.objects.create_user(username, password, email)
		new_user.is_active = False
		new_user.save()
		salt = sha.new(str(random.random())).hexdigest()[:5]
		activation_key = sha.new(salt + username).hexdigest()
		cls.objects.create(user=username, activation_key=activation_key)
		return new_user

	@classmethod
	def activate_user(cls, activation_key):
		try:
			cls.objects.get(activation_key=activation_key)
		except cls.DoesNotExist:
			return False
		# HERE: delete key from database if it exists 
		return True