
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
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

@csrf_exempt
def  qiushi_list(request):
	if request.method == 'GET':
		spyder = SpyderQiushi()
		for aStory in spyder.getStorys(1):
				newqiuShi = qiuShi(content = str(aStory.content), image = str(aStory.image), author = str(aStory.author))
				newqiuShi.save()
		qiushiList = qiuShi.objects.all()
		serializer = QiushiSerializer(qiushiList,many=True)
		return JSONResponse(serializer.data)
		# else:	
		# 	print('NO')
		# 	serializer = QiushiSerializer(qiushiList,many=True)
		# 	return JSONResponse(serializer.data)
	else:
		return HttpResponse(status = 404)

@csrf_exempt
def  qiushi_detail(request,pk):
	try:
		qiushi = qiuShi.objects.get(pk=pk)
	except qiuShi.DoseNotExist:
		return HttpResponse(status = 404)

	if request.method == 'GET':
		serializer = QiushiSerializer(qiushi)
		return JSONResponse(serializer.data)
	else :
		return HttpResponse(status = 404)
