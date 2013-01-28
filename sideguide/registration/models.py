import sha
import random
import datetime

from django.db import models
from django import forms
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.forms import UserCreationForm
from django.template.loader import render_to_string

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=75,
        label='Email')
    accept_terms_and_privacy = forms.BooleanField(
            error_messages={'required': 'Please read and agree to the Terms of Service and Privacy Policy.'})

    def save(self):
        new_user = ActivationProfile.create_inactive_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
        )
        return new_user

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)

class ActivationProfile(models.Model):
    MAX_ACTIVATION_DAYS = 10
    
    user = models.CharField(max_length=30)
    activation_key = models.CharField(max_length=40)

    def __unicode__(self):
        return "Activation information for %s" % self.username

    @classmethod
    def create_inactive_user(cls, username, password, email, send_email=True):
        new_user = User.objects.create_user(username=username, password=password, email=email)
        new_user.is_active = False
        new_user_profile = UserProfile(
            user=new_user,
        ).save()
        new_user.save()

        salt = sha.new(str(random.random())).hexdigest()[:5]
        activation_key = sha.new(salt + username).hexdigest()
        cls.objects.create(user=username, activation_key=activation_key)
        
        if send_email:
            from django.core.mail import send_mail
            
            subject = 'Activate Your Account at OpenArt'
            message = render_to_string('registration/activation_email.html',
                {'activation_key' : activation_key,
                'expiration_days' : ActivationProfile.MAX_ACTIVATION_DAYS})
            send_mail(subject, message, 'from@example.com', [email])

        return new_user

    @classmethod
    def activate_user(cls, activation_key):
        try:
            existing_profile = cls.objects.get(activation_key=activation_key)
        except cls.DoesNotExist:
            return False
        if existing_profile.activation_key_expired():
            return False
        else:
            user_for_activation = User.objects.get(username=existing_profile.user)
            user_for_activation.is_active = True
            user_for_activation.save()
            # existing_profile.delete()
            return True

    def activation_key_expired(self):
        expiration_date = datetime.timedelta(days=ActivationProfile.MAX_ACTIVATION_DAYS)
        return (User.objects.get(username=self.user).date_joined 
            + expiration_date
            <= datetime.datetime.now())
