# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     serializers
   Description :
   Author :       7326
   date：          2017/12/18
-------------------------------------------------
   Change Activity: 2017/12/18
-------------------------------------------------
"""
__author__ = '7326'

from rest_framework import serializers
from .models import Article,Tag,Category

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'body', 'created_time', 'modified_time', 'excerpt', 'category', 'tags','author')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"