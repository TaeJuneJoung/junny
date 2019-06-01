from django.db import models
from django.conf import settings

# Create your models here.
class Junny(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    long_url = models.TextField()
    short_url = models.TextField(unique=True)
    access_time = models.DateTimeField(auto_now_add=True)
