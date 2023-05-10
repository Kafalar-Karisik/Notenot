from django.db import models
from django.utils import timezone

import datetime


# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=20, default=" ")
    note = models.CharField(max_length=500)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return print(f"{self.title}: {self.note}")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
