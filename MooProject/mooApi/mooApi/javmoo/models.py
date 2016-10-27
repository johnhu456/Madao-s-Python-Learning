
# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Actress(models.Model):
    #姓名：
    name = models.CharField("Name",max_length=100,blank=False)
    #生日
    birth = models.DateField("Birthday",auto_now=False,auto_now_add=False,blank=True)
    #年龄
    age = models.PositiveSmallIntegerField("Age",blank=True)
    #身高
    height = models.PositiveSmallIntegerField("Height",blank=True,default='')
    #罩杯
    cup = models.CharField("Cup", max_length=1, blank=True, default='')
    #胸围
    bust = models.PositiveSmallIntegerField("Bust",blank=True,default='')
    #腰围
    waist = models.PositiveSmallIntegerField("Waist circumference",blank=True,default='')
    #t臀围
    hips = models.PositiveSmallIntegerField("Hips",blank=True,default='')
    #出生地
    city = models.CharField("Place Of Birth",max_length=100,blank=True)
    #爱好
    hoby = models.CharField("Hobbies",max_length=200,blank=True)
    #该数据创建时间，不返回给用户
    created = models.DateTimeField(auto_now_add=True)
    ##UUID
    uuid = models.UUIDField(max_length=200,blank=False)
    class Meta:
        ordering = ('uuid','created','name',)

#
# class AVOverview(models.Model):
#     # 唯一标识
#     uuid = models.CharField(max_length=100, blank=True , default='',primary_key=True)
#     # 片名
#     title = models.CharField(max_length=300,blank=True,default='')
#     # 封面图片
#     coverUrl = models.CharField(max_length=300),blank=True,default='')
#     # 番号
#     code = models.CharField(max_length=100),blank=True,default='')
#     # 发行日期
#     pubDate = models.DateField(auto_now=False,auto_now_add=False)
#     class Meta:
#         ordering = ('date','code','uuid',)

