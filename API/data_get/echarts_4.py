import random
from django.http import JsonResponse
from rest_framework.views import  APIView
from database import models
from django.db.models import Sum





class Echarts4(APIView):

    def get(self, request):
        data = {}

        x_list = []
        y_list = []
        bl_list = []

        try:

            res_obj = models.History.objects.order_by('-danmaku')

            total = res_obj[0:9].aggregate(total=Sum("danmaku"))

            danmaku_total = total.get('total')

            for obj in res_obj[0:9]:
                x_list.append(obj.title[0:16] + "...")
                y_list.append(obj.danmaku)
                bl_list.append( round((obj.danmaku / danmaku_total) * 100,2) )

            data['x_list'] = x_list[::-1]
            data['y_list'] = y_list[::-1]
            data['bl_list'] = bl_list[::-1]

            return JsonResponse(data)

        except Exception as e:
            # print(e)
            data['code'] = 444
            return JsonResponse(data)



