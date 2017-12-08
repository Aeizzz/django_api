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
from rest_framework.response import Response
from django.contrib import auth
__author__ = '7326'
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from .serializers import UserLoginSerializer,UserRedisterSerializer
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

# 注册用户API
class UserRegisterAPI(APIView):
    @csrf_exempt
    def post(self,request):
        serializer = UserRedisterSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            try:
                User.objects.get(username=data['username'])
            except User.DoesNotExist:
                pass
            try:
                User.objects.get(studentid=data['studentid'])
                JSONResponse({}, status=500)
            except User.DoesNotExist:
                user = User.objects.create(username=data['username'],name=data['name'],studentid=data['studentid'],
                                    phone=data['phone'],major=data['major'],grade=data['grade'],sex=data['sex'])
                user.set_password(data['password'])
                user.save()
                return JSONResponse({'msg':'注册成功'},status=200)
        else:
            return JSONResponse(serializer.errors,status=500)


        '''
        注册json api接口
        '''
        pass


# 登陆API(未完成)
class UserLoginAPI(APIView):
    @csrf_exempt
    def post(self,request):
        re_data = {
            'msg':'',
            'code':'',
            'user':'',
        }
        data = request.data
        user = auth.authenticate(username=data['username'],password=data['password'])
        re_data = {
            'msg':'',
            'code':'',
        }
        if user:
            auth.login(request,user)
            re_data['msg'] = '登陆成功'
            re_data['code'] = 200
            re_data['user'] = {
                'username':user.username,
                'name':user.name,
                'avatar':'https://raw.githubusercontent.com/taylorchen709/markdown-images/master/vueadmin/user.png'
            }
            return JSONResponse(re_data,status=200)
        else:
            re_data['msg'] = 'Invalid username or password'
            re_data['code'] = 404
            return JSONResponse(re_data)


class UserLogoutAPI(APIView):
    def get(self, request):
        auth.logout(request)
        return JSONResponse({'code':200,'msg':'ok'})

# 获取所有用户api
class UserListAPI(APIView):
    @csrf_exempt
    def get(self,request):
        user_list = User.objects.all()
        num = User.count()
        print(user_list)
        re_data = {
            'total':num,
            'users':'',

        }
        return JSONResponse(re_data,status=200)
