from django.db import models

# Create your models here.
class Junny(models.Model):
    long_url = models.TextField()
    short_url = models.TextField(unique=True)
    access_time = models.DateTimeField(auto_now_add=True)