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
from .models import User,Link
from .serializers import (UserLoginSerializer, UserSerializer,UserRegisterSerializer,CrateLinkSerializer,EditLinkSerializer,LinkBaseSerializer)



class UserRegisterAPI(APIView):
    @validate_serializer(UserRegisterSerializer)
    def post(self,request):
        data = request.data
        user = User.objects.create(username=data['username'],name=data['name'])
        user.set_password(data['password'])
        user.save()
        return self.success('Success')


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



class LinkAPI(APIView):
    @validate_serializer(CrateLinkSerializer)
    def post(self,request):
        data = request.data
        link = Link.objects.create(data)
        return self.success()

    def get(self,request):
        links = Link.objects.all()
        self.success(EditLinkSerializer(links,many=True).data)

    @validate_serializer(EditLinkSerializer)
    def put(self,request):
        data = request.data
        link_id = data.pop('id')
        try:
            link = Link.objects.get(id=link_id)
        except Link.DoesNotExist:
            return self.error('link Dose Not Exist')

        for k,v in data.items():
            setattr(link,k,v)
        link.save()
        return self.success()

    def delete(self,request):
        id = request.GET.get('id')
        try:
            link = Link.objects.get('id')
        except Link.DoesNotExist:
            return self.error('link Dose Not Exist')
        link.delete()
        return self.success()




