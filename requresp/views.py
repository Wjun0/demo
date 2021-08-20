from itertools import chain

from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from requresp.serializers import StudentSerizlizers
from users.models import Student, Emp
import random
from django.db import transaction
import datetime
import django.utils.timezone

def getquerystring(request):
    '''
    演示接收查询字符串参数
    :param request:
    :return:
    '''
    # 获取查询字符串参数:
    querydict = request.GET
    a = querydict.get('a')
    blist = querydict.getlist('b')

    # 打印:
    print(a)
    print(blist)

    return HttpResponse('getquerystring')



class Student_index(GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerizlizers

    def get(self,request):
        queryset = self.get_queryset()
        # queryset = queryset.filter(sname='注册')

        res_queryset = []
        list = ['t2',"t3"]
        res_queryset = queryset.filter(sname__icontains=[list[0]])
        for i in list:
            # res_queryset.append(queryset.filter(sname__icontains=i))
            res_queryset = queryset.filter(sname__icontains=i) | res_queryset
        # queryset = chain(res_queryset)
        ser = self.get_serializer(res_queryset, many=True)
        return Response(ser.data)


    def post(self,request):
        random_name = [ ["t1",'t2',"t3"],
                        ["t1","t4"],
                        ["t2"],
                        [],
                        ["t1","t3"]
        ]
        item_list = []
        for i in range(4000,5000):
            item = {
                'sno': i,
                'sname': random.choice(random_name),
                'ssex': random.choice(['男', '女']),
                'sbirthday': '2021-02-02 0:0:0',
                'sclass': '9000'
            }
            item_list.append(Student(**item))
        Student.objects.bulk_create(item_list)


        # item = {
        #     'sno': 333,
        #     'sname': random.choice(random_name),
        #     'ssex': random.choice(['男','女']),
        #     'sbirthday': '2021-02-02 0:0:0',
        #     'sclass': '9000'
        # }
        #
        # serailizer = self.get_serializer(data=item)
        # serailizer.is_valid(raise_exception=True)
        # serailizer.save()

        # with transaction.atomic():
        #     for i in range(1,20000):
        #         item = {
        #             'sno':i,
        #             'sname':random.choice(random_name),
        #             'ssex':random.choice(['男','女']),
        #             'sbirthday':datetime.datetime.now(),
        #             'sclass': i
        #         }
        #
        #         serailizer = self.get_serializer(data=item)
        #         serailizer.is_valid(raise_exception=True)
        #         serailizer.save()

        return Response({'message':'ok'})

    def delete(self,request):
        queryset = self.get_queryset()
        with transaction.atomic():
            queryset.filter(sno__gt=1).delete()
        return Response({'message':'ok'})

    def put(self,request):
        obj = self.get_queryset().get(sno=1)
        dic = {'ssex':'女'}
        ser = self.get_serializer(instance=obj,data=dic,)
        ser.is_valid(raise_exception=True)
        print(ser.error)
        ser.save()
        return Response({'message':'ok'})



class EmpAPI(APIView):
    def get(self,request):
        duty = ['初级程序员']
        Emp.objects.filter(deptno="01").filter(~Q(duty__in=duty)).update(sal=3500)
        return Response({"message":"ok"})

