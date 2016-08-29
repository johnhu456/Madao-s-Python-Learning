# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class qiuShi(models.Model):
	created = models.DateTimeField(auto_now_add = True)
	content = models.TextField()
	author = models.TextField()
	image = models.TextField()
	class Meta:
		ordering = ['created',] 
# Create your models here.
