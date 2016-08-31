
from django.shortcuts import render
from rest_framework import status
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from baikeApi.models import qiuShi
from baikeApi.serializers import QiushiSerializer
from baikeApi.spyderBaike import QiushiStory,SpyderQiushi
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class JSONResponse(HttpResponse):
		def __init__(self,data,**kwargs):
			content = JSONRenderer().render(data)
			kwargs['content_type'] = 'application/json'
			super(JSONResponse,self).__init__(content,**kwargs)

@api_view(['GET','POST'])
def  qiushi_list(request):
	if request.method == 'GET':
		spyder = SpyderQiushi()
		for aStory in spyder.getStorys(1):
				newqiuShi = qiuShi(content = str(aStory.content), image = str(aStory.image), author = str(aStory.author))
				newqiuShi.save()
		qiushiList = qiuShi.objects.all()
		serializer = QiushiSerializer(qiushiList,many=True)
		return Response(serializer.data)
		# else:	
		# 	print('NO')
		# 	serializer = QiushiSerializer(qiushiList,many=True)
		# 	return JSONResponse(serializer.data)
	else:
		return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def  qiushi_detail(request,pk):
	try:
		qiushi = qiuShi.objects.get(pk=pk)
	except qiuShi.DoseNotExist:
		return Response(status = status.HTTP_400_BAD_REQUEST)

	if request.method == 'GET':
		serializer = QiushiSerializer(qiushi)
		return Response(serializer.data)
	else :
		return Response(status = status.HTTP_400_BAD_REQUEST)
