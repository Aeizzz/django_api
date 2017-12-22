from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from .models import Article,Tag,Category
from .serializers import ArticleSerializer,TagSerializer
from utils.api.api import APIView
class JSONResponse(HttpResponse):
    """docstring for JSONRenderer"""
    '''
    将HttpResponse对象相应的内容转化为json
    '''

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json;charset=utf-8'
        super(JSONResponse, self).__init__(content, **kwargs)

# Create your views here.
class ArticleAPI(APIView):
    @csrf_exempt
    def post(self,request):

        pass
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

        # 分页查询
        data = self.paginate_data(request,articles,ArticleSerializer)
        # 返回数据
        return self.success(data)
        pass
    @csrf_exempt
    def put(self,request):
        pass
    @csrf_exempt
    def delete(self,request):
        pass


class TagAPI(APIView):
    @csrf_exempt
    def get(self, request):
        '''
        获取所有的tag
        :param request:
        :return:
        '''
        tags = Tag.objects.all()
        return self.success(TagSerializer(tags, many=True).data)