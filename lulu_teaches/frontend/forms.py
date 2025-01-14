# forms.py
from django import forms
from django.contrib.auth.models import User
from lulu_teacher import models


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password','is_staff']

class LuluTrainningForm(forms.ModelForm):
    class Meta:
        model = models.luluTrainning
        fields = ['version_title', 'attachments', 'comments']
        widgets ={
            'comments': forms.Textarea(attrs={'rows':3}),
        }