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

class UserManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, username):
        return self.get(**{f"{self.model.USERNAME_FIELD}__iexact": username})



class User(AbstractBaseUser):
    username = models.CharField(max_length=20,unique=True)
    studentid = models.CharField(max_length=20,blank=True)
    name = models.CharField(max_length=20,blank=True)
    phone = models.CharField(max_length=20,blank=True)
    major = models.CharField(max_length=20,blank=True)
    grade = models.CharField(max_length=20,blank=True)
    sex = models.CharField(max_length=20,blank=True)

    objects = UserManager()
    USERNAME_FIELD = "username"
    class Meta:
        db_table='user'