import random
import time

from django.test import TestCase

# Create your tests here.


from peewee import *
from playhouse.pool import PooledMySQLDatabase

# if __name__ == '__main__':
# #     print('hello')



import threading
import logging




def run(id):
    for i in range(id):
        print(i,id)
        time.sleep(2)


def xss_test():
    from django.utils.html import strip_tags

    str = "Hello <?>  <b><i>world!</i></b> <?>"
    data = strip_tags(str)
    print(data)

    s2 = """<? php="test" >','<?>"""
    d2 = strip_tags(s2)
    print(d2)

if __name__ == '__main__':
    xss_test()

    import datetime
    a = 0
    b = 0
    c = a + b
    if c =="0":
        print(0)
    else:
        print(1)
    dt = datetime.datetime.now()
    print(f"{dt} xxx")
    print(datetime.datetime.now())

    # logging.basicConfig(format='[%(asctime)s] %(message)s',level=logging.INFO)
    # logg = logging.getLogger(__name__)
    #
    # logg.info('hello')
    # print(logg.info('hello '))

    # threading.Thread(run(10)).start()
    # threading.Thread(run(20)).start()
    # threading.Thread(run(30)).start()
    # r1 = run(10)
    # r2 = run(20)
    # r1.send(None)
    # r2.send(None)




