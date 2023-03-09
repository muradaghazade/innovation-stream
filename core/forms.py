from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import Subscriber
from django.core.exceptions import ValidationError

class SubscriberForm(forms.ModelForm):
    email = forms.EmailField(max_length=125, widget=forms.EmailInput(attrs={
        'class': 'form-inp', 
        'placeholder': 'Enter Email'
    }), )

    class Meta:
        model = Subscriber
        fields = (
            'email',
        )