import random
from django.http import JsonResponse
from rest_framework.views import  APIView
from database import models
from django.db.models import Sum





class Total(APIView):

    def get(self, request):

        data = {}

        try:
            view_raw = models.History.objects.order_by('id').aggregate(total=Sum("view"))
            data['view'] = view_raw.get('total')
            return JsonResponse(data)

        except Exception as e:
            # print(e)
            data['code'] = 444
            return JsonResponse(data)



