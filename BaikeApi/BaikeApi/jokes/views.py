from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from jokes.models import Joke
from Serializer.serializers import JokeSerializer

# from rest_framework.parsers import JSONParser
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt



# class JSONResponse(HttpResponse):
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)

# @csrf_exempt
# @api_view(['GET','POST'])
# def joke_list(request,format=None):
#     if request.method == 'GET':
#         jokes = Joke.objects.all()
#         serializer = JokeSerializer(jokes,many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = JokeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET'])
# def joke_detail(request,id,format=None):
#     try:
#         joke = Joke.objects.get(id=id)
#     except Joke.DoesNotExists:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = JokeSerializer(joke)
#         return Response(serializer.data)
#     # elif request.method == 'POST':

class JokeList(APIView):
    def get(self,request,format=None):
        jokes = Joke.objects.all()
        serializer = JokeSerializer(jokes, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = JokeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class JokeDetail(APIView):
    def get_object(self,id):
        try:
            return Joke.objects.get(id=id)
        except Joke.DoesNotExists:
            raise Http404
    def get(self,request,id,format=None):
        joke = self.get_object(id)
        serializer = JokeSerializer(joke)
        return Response(serializer.data)

