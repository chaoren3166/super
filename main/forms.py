#-*- coding: utf-8 -*-
from django import forms
from models import User

__author__ = 'weichao02'


class UserForm(forms.ModelForm):

    class Meta:
        model = User


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    my_img = forms.FileField()
