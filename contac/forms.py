from dataclasses import fields
from django import forms
from django.forms import ModelForm

from contac.models import Contact


class ContacForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('date',)
