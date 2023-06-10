from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
class SignupForm(UserCreationForm):
    instagram_username=forms.CharField(max_length=100)
    instagram_profile_link=forms.URLField(max_length=150)
    phone_number =forms.CharField(max_length=10)
    class Meta:
        model=CustomUser
        fields=["username","instagram_username","instagram_profile_link","phone_number","password1","password2"]