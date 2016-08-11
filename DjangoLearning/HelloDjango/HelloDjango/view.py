# -*- coding: utf-8 -*-
# from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	context = {}
	context['hello'] = "试试这是什么"
	return render(request,'hello.html',context)