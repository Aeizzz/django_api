from django.db import models
from account.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)



class Tag(models.Model):
    name = models.CharField(max_length=64)


class Article(models.Model):
    # 标题
    title = models.CharField(max_length=70)
    # 正文
    body = models.TextField()
    # 创建时间修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    # 摘要
    excerpt = models.CharField(max_length=200, blank=True)
    #
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    #用户
    author = models.ForeignKey(User,on_delete=models.CASCADE)
