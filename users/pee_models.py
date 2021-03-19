from peewee import *
from peewee import __exception_wrapper__
from playhouse.pool import PooledMySQLDatabase

# db = PooledMySQLDatabase(
#     'sql_test',
#     max_connections=8,
#     stale_timeout=5,
#     user='root',
#     password='mysql',
#     timeout=8,
# )


class RetryOperationalError(object):
    def execute_sql(self, sql, params=None, commit=True):
        try:
            cursor = super(RetryOperationalError, self).execute_sql(sql, params, commit)
        except OperationalError:
            if not self.is_closed():
                self.close()
            with __exception_wrapper__:
                cursor = self.cursor()
                cursor.execute(sql, params or ())
                if commit and not self.in_transaction():
                    self.commit()
        return cursor


class RetryMySQLDatabase(RetryOperationalError, MySQLDatabase):
    pass




database = RetryMySQLDatabase('sql_test', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'password': 'mysql'})
# database = MySQLDatabase('sql_test', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'password': 'mysql'})



class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database
        # database = db

class Teacher(BaseModel):
    depart = CharField()
    prof = CharField(null=True)
    tbirthday = DateTimeField(null=True)
    tname = CharField()
    tno = CharField(primary_key=True)
    tsex = CharField()

    class Meta:
        table_name = 'teacher'

class Course(BaseModel):
    cname = CharField()
    cno = CharField()
    tno = ForeignKeyField(column_name='tno', field='tno', model=Teacher)

    class Meta:
        table_name = 'course'

class DjangoMigrations(BaseModel):
    app = CharField()
    applied = DateTimeField()
    name = CharField()

    class Meta:
        table_name = 'django_migrations'

class Emp(BaseModel):
    deptno = CharField(null=True)
    duty = CharField(null=True)
    empid = AutoField()
    name = CharField(null=True)
    sal = CharField(null=True)

    class Meta:
        table_name = 'emp'

class Grade(BaseModel):
    low = IntegerField(null=True)
    rank = CharField(null=True)
    upp = IntegerField(null=True)

    class Meta:
        table_name = 'grade'
        primary_key = False

class Score(BaseModel):
    cno = CharField()
    degree = CharField()
    sno = CharField()

    class Meta:
        table_name = 'score'
        primary_key = False

class Student(BaseModel):
    sbirthday = DateTimeField(null=True)
    sclass = CharField(null=True)
    sname = CharField()
    sno = CharField(primary_key=True)
    ssex = CharField()

    class Meta:
        table_name = 'student'

