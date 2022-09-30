import time

from django.db import transaction
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import serializers
from app2_de2_test.models import Db2_users

from concurrent.futures import ThreadPoolExecutor

def send_email(data):
    time.sleep(10)
    print(data)
    time.sleep(10)
    print("sssssssssssssssss")


def user(request):
    print("use")
    user = []
    objs = Db2_users.objects.using("db2").all()
    for i in objs:
        user.extend(i.name.split(','))
    print(user)
    obj = Db2_users.objects.all()
    resp = Db2_users.objects.filter(name="wang_update").order_by("age").first()
    return JsonResponse(['db2'],safe=False)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Db2_users
        fields = "__all__"


class UserList(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = Db2_users.objects.all()


class UserRetrive(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = Db2_users.objects.all()


class UserUpdate(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = Db2_users.objects.all()
    # def get(self,reqeust):
    #     app_users = [user.name for user in Db2_users.objects.all()]
    #     return Response(app_users)


    # def patch(self, request, *args, **kwargs):
    #     pass
    #
    # def put(self, request, *args, **kwargs):
    #     pass

class Update_db2_user(APIView):
    def get(self,requests):
        info = {
            'name':"wang_update",
            "age":"1112",
            'email':"111@111.com"
        }
        res = Db2_users.objects.update_or_create(
            name=info.get("name","xx"),
            age = info.get("age"),
            defaults=info
        )
        return Response({"update":"ok"})

class TransactionTestAPI(APIView):
    def get(self,request):
        num = 1
        with transaction.atomic(using='db2'):
            point_id = transaction.savepoint()
            try:       # try 中的代码不会在事务中
                num += 1
                transaction_test = "transaction_test"
                info = {
                    'name': "transaction_test",
                    "age": "1112",
                    'email': "111@111.com"
                }
                data = Db2_users.objects.create(**info)
                print(data.id)
                d = Db2_users.objects.filter(name=transaction_test).first()
                print(d.name)
                print(1/0)          #  触发异常回滚
            except:
                print("error")
                transaction.savepoint_rollback(point_id)  # 即使使用回滚，因为在try中，所以不会回滚
        print(num)  # 在事务中的修改即使事务回滚了，对变量的修改也不会回滚，只会回滚对数据库的操作
        return Response({"message":"ok"})
