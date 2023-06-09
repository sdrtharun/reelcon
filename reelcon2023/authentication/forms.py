from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignupForm(UserCreationForm):
    instagram_username=forms.CharField()
    instagram_profile_link=forms.URLField()
    class Meta:
        model=User
        fields=["username","instagram_username","instagram_profile_link","password1","password2"]