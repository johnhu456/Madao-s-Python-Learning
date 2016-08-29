# -*- coding:utf-8 -*-
from baikeApi.models import qiuShi
from rest_framework import serializers

class QiushiSerializer(serializers.ModelSerializer):
		class Meta:
			model = qiuShi
			fields = ('content','author','image')