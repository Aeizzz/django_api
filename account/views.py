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
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

__author__ = '7326'
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from .serializers import UserLoginSerializer
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


class UserRegisterAPI(APIView):
    @csrf_exempt
    def post(self,request):
        '''
        注册json api接口
        '''
        pass



class UserLoginAPI(APIView):
    @csrf_exempt
    def post(self,request):
        re_data = {
            'msg':'',
            'code':'',
            'user':'',
        }
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            try:
                user = User.objects.get(username=data['username'])
                re_data['msg'] = '登陆成功'
                re_data['code'] = 200
                re_data['user'] = data
                return JSONResponse(re_data,status=200)
            except User.DoesNotExist:
                re_data['msg'] = '用户不存在'
                re_data['code'] = 500
                re_data['user']=''
                return JSONResponse(re_data,status=500)
        else:
            return JSONResponse(serializer.errors,status=500)


class UserListAPI(APIView):
    @csrf_exempt
    def get(self,request):
        user_list = User.objects.all()
        user_list_g = []
        for user in user_list:
            user_list_g.append({'name':user.username,'phone':user.phone})

        re_data = {
            'total':len(user_list_g),
            'users':user_list_g
        }
        return JSONResponse(re_data,status=200)