import random

from django.http import  HttpResponse
from rest_framework.views import  APIView
from database import models


class Collection(APIView):

    def get(self, request):

        name = request.GET.get("name")
        urls = request.GET.get("url")
        src = request.GET.get("src")
        message = {}
        try:

            models.Colect.objects.create(co_title=name,co_down_link=urls,co_down_img=src)
            return HttpResponse("收藏成功")

        except Exception as e:
            print(e)
            return HttpResponse("收藏失败，请联系管理员995405033")