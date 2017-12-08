# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     serializers
   Description :
   Author :       7326
   date：          2017/12/6
-------------------------------------------------
   Change Activity: 2017/12/6
-------------------------------------------------
"""
__author__ = '7326'


from rest_framework import serializers

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20)


class UserRedisterSerializer(serializers.Serializer):
    studentid = serializers.CharField(max_length=20)
    username = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20)
    phone = serializers.CharField(max_length=20)
    major = serializers.CharField(max_length=20)
    grade = serializers.CharField(max_length=20)
    sex = serializers.CharField(max_length=20)