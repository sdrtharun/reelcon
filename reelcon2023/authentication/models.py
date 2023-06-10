from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    instagram_username=models.CharField(max_length=100)
    instagram_profile_link=models.URLField(max_length=150)
    phone_number =models.CharField(max_length=10)