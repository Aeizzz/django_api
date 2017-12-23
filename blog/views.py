from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from .models import Article,Tags,Categorys
from .serializers import ArticleSerializer,TagSerializer,CreateArticleSerializer,EditArticleSerializer,CategorySerializer,ArticleAdminSerializer
from utils.api.api import APIView,validate_serializer
from account.models import User


class JSONResponse(HttpResponse):

    """docstring for JSONRenderer"""
    '''
    将HttpResponse对象相应的内容转化为json
    '''

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json;charset=utf-8'
        super(JSONResponse, self).__init__(content, **kwargs)


class ArticleAPI(APIView):
    @validate_serializer(CreateArticleSerializer)
    def post(self,request):
        '''
        增加文章
        :param request:
        :return:
        '''
        data = request.data
        data["author"] = request.user
        data["category"] = Categorys.objects.get(name=data['category'])
        tags = data.pop("tags")
        article = Article.objects.create(**data)
        for item in tags:
            try:
                tag = Tags.objects.get(name=item)
            except Tags.DoesNotExist:
                tag = Tags.objects.create(name=item)
            article.tags.add(tag)
        return self.success(ArticleAdminSerializer(article,many=True).data)

    @csrf_exempt
    def get(self,request):
        '''
        :param request:
        :return:
        获取文章，参数
        page: 页数
        limit: 每页数据
        offset: 偏移量
        tag: 标签
        category: 分类
        '''
        # 查询所有
        articles = Article.objects.all()
        # 查看每页的条数
        limit = request.GET.get('limit')
        if not limit:
            return self.error("Limit is needed")
        # 根据标签查询
        tag_text = request.GET.get('tag')
        if tag_text:
            articles = articles.filter(tags__name=tag_text)
        # 根据分类查询
        category_text = request.GET.get('category')
        if category_text:
            articles = articles.filter(category__name=category_text)

        # 返回数据
        return self.success(self.paginate_data(request,articles,ArticleSerializer))

    @validate_serializer(EditArticleSerializer)
    def put(self,request):
        '''
        更新文章
        :param request:
        :return:
        '''
        data = request.data
        article_id = data.pop('id')
        try:
            article = Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            return self.error("article does not exist")

        tags = data.pop('tags')

        for k,v in data.items():
            setattr(article,k,v)
        article.save()

        article.tags.remove(*article.tags.all())

        for tag in tags:
            try:
                tag = Tags.objects.get(name=tag)
            except Tags.DoesNotExist:
                Tags.objects.create(name=tag)
            article.tags.add(tag)
        return self.success()

    def delete(self,request):
        '''
        删除文章
        :param request:
        :return:
        '''
        id = request.GET.get('id')
        if not id:
            return self.error('Invalid parameter, id is requred')
        try:
            article = Article.objects.get(id=id)
        except Article.DoesNotExist:
            return self.error("article does not exists")

        article.delete()
        return self.success()
class TagAPI(APIView):
    @csrf_exempt
    def get(self, request):
        '''
        获取所有的tag
        :param request:
        :return:
        '''
        tags = Tags.objects.all()
        return self.success(TagSerializer(tags, many=True).data)

class CategoryAPI(APIView):
    def get(self,request):
        '''

        :param request:
        :return:
        '''
        category = Categorys.objects.all()
        return self.success(CategorySerializer(category,many=True).data)