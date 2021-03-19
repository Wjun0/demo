from django.db import models

# Create your models here.


class Db2_users(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'
        app_label = 'db2_test'
