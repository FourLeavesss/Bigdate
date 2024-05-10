import random
from django.http import JsonResponse
from rest_framework.views import  APIView
from database import models



class CiYunData(APIView):


    def get(self, request):
        data = {}

        res_list = []

        try:
            res_obj = models.History.objects.values("tname").distinct()
            for data in res_obj:
                json_data = {}
                if data.get('tname') != None:
                    json_data['name'] = data.get('tname')
                    json_data['value'] = random.randint(100,300)
                    res_list.append(json_data)

            data['res_list'] = res_list
            data['code'] = 200
            return JsonResponse(data)

        except Exception as e:
            print(e)
            data['code'] = 444
            return JsonResponse(data)



