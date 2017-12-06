# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     views
   Description :
   Author :       7326
   date：          2017/12/6
-------------------------------------------------
   Change Activity: 2017/12/6
-------------------------------------------------
"""
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

__author__ = '7326'

from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from .serializers import UserRegisterSerializer
import json
from .models import User

class JSONResponse(HttpResponse):
    """docstring for JSONRenderer"""
    '''
    将HttpResponse对象相应的内容转化为json
    '''

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json;charset=utf-8'
        super(JSONResponse, self).__init__(content, **kwargs)


class UserRegistAPIview(APIView):
    @csrf_exempt
    def post(self,request):
        '''
        注册json api接口
        '''
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            try:
                User.objects.get(username=data['username'])
                return JSONResponse({'status':'error','message':'用户名已存在'},status=500)
            except User.DoesNotExist:
                user = User.objects.create(username=data['username'],phone=data['phone'])
                user.set_password(data['password'])
                user.save()
                return JSONResponse({'status':'ok','message':'注册用户成功'},status=200)
        else:
            return JSONResponse(serializer.errors,status=500)



