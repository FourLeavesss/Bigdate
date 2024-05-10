import random
from django.http import JsonResponse
from rest_framework.views import  APIView
from database import models
from django.db.models import Sum





class Echarts1(APIView):

    def get(self, request):

        data = {}

        bf_total_list = []
        dm_total_list = []
        fx_total_list = []
        sc_total_list = []
        pl_total_list = []

        try:
            object_data_a = models.PieData.objects.order_by("id")
            object_data_b = models.BarData.objects.order_by("id")
            object_data_c = models.LintData.objects.order_by("id")
            object_data_d = models.BarsData.objects.order_by("id")

            # 播放
            bf_total_list.append(object_data_a.aggregate(total=Sum("view")).get('total') / 100)
            bf_total_list.append(object_data_b.aggregate(total=Sum("view")).get('total') / 100)
            bf_total_list.append(object_data_c.aggregate(total=Sum("view")).get('total') / 100)
            bf_total_list.append(object_data_d.aggregate(total=Sum("view")).get('total') / 100)
            # 弹幕
            dm_total_list.append(object_data_a.aggregate(total=Sum("danmaku")).get('total'))
            dm_total_list.append(object_data_b.aggregate(total=Sum("danmaku")).get('total'))
            dm_total_list.append(object_data_c.aggregate(total=Sum("danmaku")).get('total'))
            dm_total_list.append(object_data_d.aggregate(total=Sum("danmaku")).get('total'))
            # 分享
            fx_total_list.append(object_data_a.aggregate(total=Sum("share")).get('total'))
            fx_total_list.append(object_data_b.aggregate(total=Sum("share")).get('total'))
            fx_total_list.append(object_data_c.aggregate(total=Sum("share")).get('total'))
            fx_total_list.append(object_data_d.aggregate(total=Sum("share")).get('total'))
            # 收藏
            sc_total_list.append(object_data_a.aggregate(total=Sum("favorite")).get('total'))
            sc_total_list.append(object_data_b.aggregate(total=Sum("favorite")).get('total'))
            sc_total_list.append(object_data_c.aggregate(total=Sum("favorite")).get('total'))
            sc_total_list.append(object_data_d.aggregate(total=Sum("favorite")).get('total'))
            # 收藏
            pl_total_list.append(object_data_a.aggregate(total=Sum("reply")).get('total'))
            pl_total_list.append(object_data_b.aggregate(total=Sum("reply")).get('total'))
            pl_total_list.append(object_data_c.aggregate(total=Sum("reply")).get('total'))
            pl_total_list.append(object_data_d.aggregate(total=Sum("reply")).get('total'))


            #
            echarts_5 = []
            echarts_5.append(object_data_a.count())
            echarts_5.append(object_data_b.count())
            echarts_5.append(object_data_c.count())
            echarts_5.append(object_data_d.count())

            data['bf_total_list'] = bf_total_list
            data['dm_total_list'] = dm_total_list
            data['fx_total_list'] = fx_total_list
            data['sc_total_list'] = sc_total_list
            data['pl_total_list'] = pl_total_list

            data['echarts_5'] = echarts_5



            return JsonResponse(data)

        except Exception as e:
            # print(e)
            data['code'] = 444
            return JsonResponse(data)



