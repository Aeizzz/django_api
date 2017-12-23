# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class UserManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, username):
        return self.get(**{f"{self.model.USERNAME_FIELD}__iexact": username})



class User(AbstractBaseUser):
    username = models.CharField(max_length=20,unique=True)
    name = models.CharField(max_length=20,blank=True)

    objects = UserManager()
    USERNAME_FIELD = "username"

    class Meta:
        db_table = 'user'