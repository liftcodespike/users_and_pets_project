from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pet(models.Model):
	name = models.CharField(max_length=9000)

class User(models.Model):
	name = models.CharField(max_length=9000)
	age = models.IntegerField()
	pets = models.ManyToManyField(Pet, related_name = 'users')




