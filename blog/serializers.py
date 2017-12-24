# -*- coding: utf-8 -*-


from rest_framework import serializers
from .models import Article,Tags,Categorys
from account.models import User
from account.serializers import UserSerializer

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'body', 'category','author')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorys
        fields = "__all__"

class CreateOrEditArticleSerializer(serializers.Serializer):
    # 标题
    title = serializers.CharField(max_length=70)
    # 正文
    body = serializers.CharField()
    category = serializers.CharField()
    tags = serializers.ListField(child=serializers.CharField(max_length=32),allow_empty=False)
    author = User




class CreateArticleSerializer(CreateOrEditArticleSerializer):
    pass


class EditArticleSerializer(CreateOrEditArticleSerializer):
    id = serializers.IntegerField()


class ArticleAdminSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=70)
    body = serializers.CharField()
    category = CategorySerializer
    tags = serializers.SlugRelatedField(many=True, slug_field="name", read_only=True)
    author = UserSerializer


