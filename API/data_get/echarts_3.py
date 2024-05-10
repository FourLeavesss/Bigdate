import random
from django.http import JsonResponse
from rest_framework.views import  APIView
from database import models
from django.db.models import Sum





class Echarts3(APIView):

    def get(self, request):

        data = {}

        try:

            x_list = []
            y_list = []

            res_obj = models.History.objects.values("tname").distinct()
            for data in res_obj:
                if data.get('tname') != None:
                    x_list.append(data.get('tname'))
                    y_list.append(models.History.objects.filter(tname=data.get('tname')).count())

            data['x_list'] = x_list
            data['y_list'] = y_list

            return JsonResponse(data)

        except Exception as e:
            # print(e)
            data['code'] = 444
            return JsonResponse(data)



