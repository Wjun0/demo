from django.db import models

# Create your models here.

class Student(models.Model):
    sno = models.CharField(max_length=255,primary_key=True)
    sname = models.CharField(max_length=255)
    ssex = models.CharField(max_length=255)
    sbirthday = models.DateTimeField()
    sclass = models.CharField(max_length=255)

    class Meta:
        db_table = 'student'