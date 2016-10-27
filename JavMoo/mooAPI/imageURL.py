# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from models import AVDisc

class OverviewURL(models.Model):
    url = models.URLField("地址",max_length=300,blank=True,default='')
    disc = models.ForeignKey(AVDisc)