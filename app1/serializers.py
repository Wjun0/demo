from app_users.models import Student
from rest_framework.serializers import ModelSerializer


class StudentSerizlizers(ModelSerializer):

    class Meta:
        model = Student
        fields = ("__all__")

    def create(self,valid_data):
        print(valid_data)
        instance = super(StudentSerizlizers, self).create(valid_data)
        return instance


    def update(self,instance, valid_data):
        instance = super(StudentSerizlizers, self).update(instance,valid_data)

        return instance

