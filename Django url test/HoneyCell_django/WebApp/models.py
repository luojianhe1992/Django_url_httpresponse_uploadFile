from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

def generate_filename(self, filename):
    url = 'documents/%s/%s' %(self.user.username, filename)
    return url

class Task(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    docfile = models.FileField(upload_to=generate_filename)

