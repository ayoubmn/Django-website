from django.db import models
from datetime import datetime

# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=100)
    date_of = models.DateTimeField(max_length=20, default=datetime.now)
