from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Joke(models.Model):
	content = models.CharField(max_length=200, blank=True, default='')
	author = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering = ('created',)