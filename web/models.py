from __future__ import unicode_literals

from django.db import models

class Message(models.Model):
        user = models.CharField(max_length=50)
        subject = models.CharField(max_length=200)
        publication_date = models.DateTimeField()
        
        def __unicode__(self):
                return self.subject
# Create your models here.
