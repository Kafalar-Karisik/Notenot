from django.db import models
from django.utils import timezone

import datetime


# Create your models here.

class Note(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    title = models.CharField(max_length=20, default="")
    note = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)  # q.pub_date = datetime.datetime(YYYY, M, D, C, M, S, MSMSMS, \
    # tzinfo=datetime.timezone.utc)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
