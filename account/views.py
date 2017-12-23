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

from django.contrib import auth
from utils.api.api import APIView, validate_serializer
from .models import User
from .serializers import UserLoginSerializer, UserSerializer,UserRegisterSerializer



class UserRegisterAPI(APIView):
    @validate_serializer(UserRegisterSerializer)
    def post(self,request):
        data = request.data
        user = User.objects.create(username=data['username'],name=data['name'])
        user.set_password(data['password'])
        user.save()
        return self.success('Success')


# 登陆API(未完成)
class UserLoginAPI(APIView):
    @validate_serializer(UserLoginSerializer)
    def post(self, request):
        data = request.data
        user = auth.authenticate(username=data['username'],password=data['password'])
        if user:
            auth.login(request,user)
            return self.success()
        else:
            return self.error("Invalid username or password")


class UserLogoutAPI(APIView):
    def get(self, request):
        auth.logout(request)
        return self.error()

# 查询用户

class UserListAPI(APIView):
    def get(self, request):
        name = request.GET.get('name')
        if name != '' and name != None:
            user_list = User.objects.filter(name=name)
        else:
            user_list = User.objects.all()
        return self.success(self.paginate_data(request,user_list,UserSerializer))





