import random
from django.http import JsonResponse
from rest_framework.views import  APIView
from database import models
from django.db.models import Sum





class Echarts2(APIView):

    def get(self, request):

        json_data = {}

        try:
            time_list = []
            xa_list = []
            res_obj = models.History.objects.order_by("pubdate").values("pubdate")
            for data in res_obj:
                times = str(data.get('pubdate').strftime('%Y-%m-%d'))
                if times not in time_list:
                    time_list.append(times)

            for data in time_list:
                xa_list.append(models.History.objects.filter(pubdate=data).count())

            json_data['time_list'] = time_list
            json_data['xa_list'] = xa_list

            return JsonResponse(data)

        except Exception as e:
            # print(e)
            json_data['code'] = 444
            return JsonResponse(json_data)



