import random
from django.http import JsonResponse
from rest_framework.views import  APIView
from lxml import etree
from database import models
from django.contrib.auth.models import AbstractUser



class Recommend(APIView):

    def get(self, request):

        data = {}

        try:
            # 推荐部分
            import numpy as np
            import math
            def make(data, n):
                # 二值化处理 n为长度
                rea_data = np.zeros(n + 1, dtype=np.int)
                # 将所选号码填充为1
                rea_data[data] = 1
                return rea_data

            try:
                # 这里传进去的已经是二值化数据
                def calculation(mine, other):
                    # 分子
                    fenzi = 0
                    for x in range(len(mine)):
                        fenzi = fenzi + mine[x] * other[x]
                    fenmu1 = 0
                    for x in range(len(mine)):
                        fenmu1 = fenmu1 + mine[x] * mine[x]
                    fenmu1 = math.sqrt(fenmu1)
                    fenmu2 = 0
                    for x in range(len(other)):
                        fenmu2 = fenmu2 + other[x] * other[x]
                    fenmu2 = math.sqrt(fenmu2)
                    # 计算权重
                    cos_th = fenzi / (fenmu1 * fenmu2)
                    return cos_th
                # 这里做协同过滤
                uname = request.COOKIES.get('uname', '')
                user_id_ds = AbstractUser.objects.get(uname=uname).pk
                gid = ""
                # 当前用户浏览数组
                user_look_list = []
                user_look_obj = models.Colect.objects.filter(user_id=user_id_ds).values("obj_id")
                for good_id in user_look_obj:
                    user_look_list.append(good_id.get("obj_id"))
                good_id = gid
                # 创建排序组
                sort_user_pk_list = []
                # 收藏组
                look_list_all = []
                user_all = AbstractUser.objects.values("pk").all()
                for user_obj in user_all:
                    if user_obj.get("pk") != user_id_ds:
                        sort_user_pk_list.append(user_obj.get("pk"))
                        look_list_obj_other = models.Colect.objects.filter(user_id=user_obj.get("pk")).values(
                            "obj_id")
                        other_look_list = []
                        for look_id in look_list_obj_other:
                            other_look_list.append(look_id.get("obj_id"))
                        look_list_all.append(other_look_list)
                # 获取最后一个PK 作为总数
                good_count = models.Colect.objects.all().order_by("-id").values("pk")
                # print("good_count",int(good_count[0].get("pk")))
                # 计算二值化
                user_binaryzation_list = make(user_look_list, int(good_count[0].get("pk")))
                # 计算最推荐值
                list_res = []
                for data in look_list_all:
                    list_res.append(calculation(user_binaryzation_list, make(data, int(good_count[0].get("pk")))))
                max_index = list_res.index(max(list_res))
                # 筛选出最匹配的
                res_user_id = sort_user_pk_list[max_index]
                goods_id_set = models.Colect.objects.filter(user_id=res_user_id).values("obj_id")
                news = []
                for good_ids in goods_id_set:
                    res = models.Colect.objects.get(pk=good_ids.get("obj_id"))
                    news.append(res)
            except:
                res = models.Colect.objects.all().order_by('?')
                res_list = []
                for obj in res[0:4]:
                    dict = {}
                    dict['name'] = obj.co_title[0:25] + "..."
                    dict['url'] = obj.co_down_link
                    res_list.append(dict)

            data['code'] = 200
            data['res_list'] = res_list

            return JsonResponse(data)

        except Exception as e:
            # print(e)
            data['code'] = 444
            return JsonResponse(data)



