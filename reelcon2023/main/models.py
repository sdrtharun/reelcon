from django.db import models

# Create your models here.
class Countdown(models.Model):
    end_time = models.DateTimeField()