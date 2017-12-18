from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from rest_framework.renderers import JSONRenderer
from .models import Article
from .serializers import ArticleSerializer
class JSONResponse(HttpResponse):
    """docstring for JSONRenderer"""
    '''
    将HttpResponse对象相应的内容转化为json
    '''

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json;charset=utf-8'
        super(JSONResponse, self).__init__(content, **kwargs)

# Create your views here.
class ArticleAPI(APIView):
    @csrf_exempt
    def post(self,request):

        pass
    @csrf_exempt
    def get(self,request):
        Article.objects.all()

        pass
    @csrf_exempt
    def put(self,request):
        pass
    @csrf_exempt
    def delete(self,request):
        pass