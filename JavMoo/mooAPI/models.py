# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from imageURL import OverviewURL

#演员
class Actress(models.Model):
    # 姓名：
    name = models.CharField("姓名", max_length=100, blank=False, default='')
    # 生日
    birth = models.DateField("生日", auto_now=False, auto_now_add=False, blank=True, null=True)
    # 年龄
    age = models.PositiveSmallIntegerField("年龄", blank=True, default='0')
    # 身高
    height = models.PositiveSmallIntegerField("身高", blank=True, default='0')
    # 罩杯
    cup = models.CharField("罩杯", max_length=1, blank=True, default='0')
    # 胸围
    bust = models.PositiveSmallIntegerField("胸围", blank=True, default='0')
    # 腰围
    waist = models.PositiveSmallIntegerField("腰围", blank=True, default='0')
    # 臀围
    hips = models.PositiveSmallIntegerField("臀围", blank=True, default='0')
    # 出生地
    city = models.CharField("出生地", max_length=100, blank=True)
    # 爱好
    hoby = models.CharField("爱好", max_length=200, blank=True)
    # 头像
    avatar = models.URLField("头像",max_length =200,blank=True,default='')
    # 该数据创建时间，不返回给用户
    created = models.DateTimeField("创建日期",auto_now_add=True)
    # UUID
    uuid = models.CharField("uuid",max_length=100,blank=False,default='-1')

    def __str__(self):
        return self.name.encode('utf-8')
    class Meta:
        ordering = ('uuid','created', 'name',)

#类组
class CategoryGroup(models.Model):
    #组名
    groupName = models.CharField("组名",max_length=100,blank=False,default='')
    # 该数据创建时间，不返回给用户
    created = models.DateTimeField("创建日期", auto_now_add=True)
    def __str__(self):
        return self.groupName.encode('utf-8')
    class Meta:
        ordering = ('created',)
#分类
class Category(models.Model):
    # 类名
    categoryName = models.CharField("类名",max_length=100,blank=False,default='')
    # UUID
    uuid = models.CharField("uuid",max_length=100,blank=False,default='-1')
    # 分组
    group = models.ForeignKey(CategoryGroup)
    # 该数据创建时间，不返回给用户
    created = models.DateTimeField("创建日期", auto_now_add=True)
    def __str__(self):
        return self.categoryName.encode('utf-8')

    class Meta:
        ordering = ('created',)

#制作商
class AVStudio(models.Model):
    #唯一标识
    uuid = models.CharField("uuid",max_length=100, blank=True , default='-1')
    #名称
    name = models.CharField("制作商",max_length=100,blank=False,default='')
    # 该数据创建时间，不返回给用户
    created = models.DateTimeField("创建日期", auto_now_add=True)
    def __str__(self):
        return self.name.encode('utf-8')

    class Meta:
        ordering = ('created',)

# 发行商
class AVPublish(models.Model):
    # 唯一标识
    uuid = models.CharField("uuid", max_length=100, blank=True, default='-1')
    # 名称
    name = models.CharField("发行商", max_length=100, blank=False, default='')
    # 该数据创建时间，不返回给用户
    created = models.DateTimeField("创建日期", auto_now_add=True)
    def __str__(self):
        return self.name.encode('utf-8')

    class Meta:
        ordering = ('created',)

#导演
class AVDirector(models.Model):
    # 唯一标识
    uuid = models.CharField("uuid", max_length=100, blank=True, default='-1')
    # 名称
    name = models.CharField("导演", max_length=100, blank=False, default='')
    # 该数据创建时间，不返回给用户
    created = models.DateTimeField("创建日期", auto_now_add=True)
    def __str__(self):
        return self.name.encode('utf-8')

    class Meta:
        ordering = ('created',)

#AV
class AVDisc(models.Model):
    # 唯一标识
    uuid = models.CharField("uuid",max_length=100, blank=True , default='-1')
    # 片名
    title = models.CharField("片名",max_length=300,blank=True,default='')
    # 小封面图片
    smallCoverUrl = models.URLField("预览",max_length=300,blank=True,default='')
    # 大封面图片
    bigCoverUrl = models.URLField("封面",max_length=300,blank=True,default='')
    # 番号
    code = models.CharField("番号",max_length=100,blank=True,default='')
    # 发行日期
    pubDate = models.DateField("发行日期",auto_now=False,auto_now_add=False,null=True)
    # 时长
    length = models.PositiveSmallIntegerField("时长",blank=True,default='0')
    #制作商
    studio = models.ForeignKey(AVStudio)
    #发行商
    publish = models.ForeignKey(AVPublish)
    #导演
    director = models.ForeignKey(AVDirector)
    #类别
    categories = models.ManyToManyField(Category)
    #演员
    actresses = models.ManyToManyField(Actress)

    class Meta:
        ordering = ('created','pubDate','code','uuid',)
