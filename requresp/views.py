from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from requresp.serializers import StudentSerizlizers
from users.models import Student
import random
from django.db import transaction
import datetime

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
        queryset = queryset.filter(sname='注册')
        ser = self.get_serializer(queryset, many=True)
        return Response(ser.data)

    def post(self,request):
        random_name = ['域名','是需','要注','册的','当域','名被','注册','信息']
        item = {
            'sno': 333,
            'sname': random.choice(random_name),
            'ssex': random.choice(['男','女']),
            'sbirthday': '2021-02-02 0:0:0',
            'sclass': '9000'
        }

        serailizer = self.get_serializer(data=item)
        serailizer.is_valid(raise_exception=True)
        serailizer.save()

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
