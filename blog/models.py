from django.db import models
from account.models import User


class Categorys(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'categorys'



class Tags(models.Model):
    name = models.CharField(max_length=64)
    class Meta:
        db_table = 'tags'


class Article(models.Model):
    # 标题
    title = models.CharField(max_length=70)
    # 正文
    body = models.TextField()
    # 创建时间修改时间
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(blank=True, null=True)
    # 摘要
    excerpt = models.CharField(max_length=200, blank=True,null=True)

    category = models.ForeignKey(Categorys,on_delete=models.CASCADE,null=True)
    tags = models.ManyToManyField(Tags, blank=True)

    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='User')

    class Meta:
        db_table = 'article'
