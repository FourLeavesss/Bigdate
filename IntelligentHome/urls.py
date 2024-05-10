"""IntelligentHome URL Configuration 995405033@qq.com

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))



    选择DJ的项目进行启动程序

    http://127.0.0.1:8080/login

    超级管理员账号密码：admin   admin123




"""
from django.conf.urls import url
from django.contrib import admin

from API import collection
from API.data_get import echarts_4, echarts_3, total, echarts_1, echarts_2, recommend, ciyun
from API.page_href import href_data
from page import data_page
from . import settings
from django.views.static import serve


urlpatterns = [

    url(r'login/', admin.site.urls),

    url(r'index', data_page.DataPage.as_view()),

    url(r'^media/(?P<path>.*)', serve, {"document_root":settings.MEDIA_ROOT}),

    url('api/collection/$', collection.Collection.as_view()),

    url('api/total$', total.Total.as_view()),  # 统计

    url(r'api/echarts4', echarts_4.Echarts4.as_view()),

    url(r'api/echarts3', echarts_3.Echarts3.as_view()),

    url(r'api/echarts1', echarts_1.Echarts1.as_view()),

    url(r'api/echarts2', echarts_2.Echarts2.as_view()),

    url(r'api/recommend', recommend.Recommend.as_view()),

    url(r'api/ciyun', ciyun.CiYunData.as_view()),


]
