from django.db import models
from django.utils import timezone
import datetime


class Gist(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    text = models.TextField()
    
    def __str__(self):
        return self.title
