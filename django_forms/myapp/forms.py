from django import forms
from django.forms import widgets
from django.forms import fields
from django.forms.fields import CharField
from .models import Snippet

class ContactForm(forms.Form):
    Mot_a_chercher = forms.CharField(widget=forms.Textarea)


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('word',)