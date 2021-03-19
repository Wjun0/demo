
from peewee import *
from peewee import __exception_wrapper__

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

Links = {
    "host": '127.0.0.1',
    "port": 3306,
    "user": 'root',
    "password": 'mysql',
    # "database" : 'sql_test',
}
# db = RetryMySQLDatabase(**Links, charset="utf8mb4")

db = MySQLDatabase('sql_test',**Links)


class BaseModel(Model):
    class Meta:
        Database = db


class Pee_Student(BaseModel):
    sno = CharField(null=True)
    sname = CharField(null=True)
    ssex = CharField(null=True)
    sbirthday = DateTimeField()
    sclass = CharField(null=True)

    class Meta:
        table_name = 'student'
