# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls
   Description :
   Author :       7326
   date：          2017/12/24
-------------------------------------------------
   Change Activity: 2017/12/24
-------------------------------------------------
"""
from django.conf.urls import url

from account.views import UserLoginAPI, UserLogoutAPI, UserRegisterAPI, UserListAPI

__author__ = '7326'

urlpatterns = [
    url(r'api/login', UserLoginAPI.as_view(), name='user_login_api'),
    url(r'api/logout', UserLogoutAPI.as_view(), name='user_logout_api'),
    url(r'api/register', UserRegisterAPI.as_view(), name='user_logout_api'),
    url(r'api/user/list', UserListAPI.as_view(), name='user_list'),
]