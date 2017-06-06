# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget
from .models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Please enter UserName'})
        self.fields['password'].widget.attrs.update(
            {'placeholder': 'Please enter Password'})


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('name', 'address', 'email', 'telephone', 'sex')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Please enter Name'})
        self.fields['address'].widget.attrs.update(
            {'placeholder': 'Please enter Address'})
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Please enter Email'})
        self.fields['telephone'].widget.attrs.update(
            {'placeholder': 'Please enter Tele'})


class LmessageForm(forms.ModelForm):

    class Meta:
        model = Lmessage
        fields=('comment','user','datetime')
