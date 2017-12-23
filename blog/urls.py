# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls
   Description :
   Author :       7326
   date：          2017/12/23
-------------------------------------------------
   Change Activity: 2017/12/23
-------------------------------------------------
"""
__author__ = '7326'

from django.conf.urls import url
from .views import ArticleAPI,TagAPI,CategoryAPI

urlpatterns = [
    url(r'api/article',ArticleAPI.as_view(),name='article_api'),
    url(r'api/tag',TagAPI.as_view(),name='tags_api'),
    url(r'api/category',CategoryAPI.as_view(),name='category_api')
]