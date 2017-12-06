# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     models
   Description :
   Author :       7326
   date：          2017/12/6
-------------------------------------------------
   Change Activity: 2017/12/6
-------------------------------------------------
"""
__author__ = '7326'

from django.db import models
from django.contrib.auth.models import AbstractBaseUser



class User(AbstractBaseUser):
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20,blank=True)
    phone = models.CharField(max_length=20,blank=True)

    class Meta:
        db_table='user'