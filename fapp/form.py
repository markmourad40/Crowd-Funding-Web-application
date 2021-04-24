from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class mymodelform(ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']

class myloginform(ModelForm):
    class Meta:
        model=User
        fields=['username','password']
