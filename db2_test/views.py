from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import serializers
from db2_test.models import Db2_users




def user(request):
    print("use")
    # obj = Db2_users.objects.using("db2").all()
    obj = Db2_users.objects.all()
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
    #     users = [user.name for user in Db2_users.objects.all()]
    #     return Response(users)


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