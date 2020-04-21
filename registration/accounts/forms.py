from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')


class UserProfileForm(forms.ModelForm):

    hostel=forms.CharField(required=True)
    class Meta():
        model=UserProfile
        fields=('hostel', 'profile_pic')
