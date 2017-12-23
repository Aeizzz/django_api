from django.conf.urls import url
from django.contrib import admin
from account.views import (UserLoginAPI,UserListAPI,UserLogoutAPI,UserRegisterAPI)
from blog.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'api/login',UserLoginAPI.as_view(),name='user_login_api'),
    url(r'api/logout',UserLogoutAPI.as_view(),name='user_logout_api'),
    url(r'api/register',UserRegisterAPI.as_view(),name='user_logout_api'),
    url(r'api/user/list',UserListAPI.as_view(),name='user_list'),


    url(r'api/article',ArticleAPI.as_view(),name='article_api')

]
