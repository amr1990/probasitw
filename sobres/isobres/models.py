from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Donor(models.Model):
    name = models.TextField(max_length=100)
    twitter = models.TextField(max_length=32)

    def __unicode__(self):
        return self.name

class Sobre(models.Model):
    amount = models.IntegerField()
    concepte = models.TextField(max_length=100)
    date = models.DateTimeField()
    donor = models.ForeignKey(Donor)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.donor.name+" - "+str(self.amount)
