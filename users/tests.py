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


if __name__ == '__main__':

    logging.basicConfig(format='[%(asctime)s] %(message)s',level=logging.INFO)
    logg = logging.getLogger(__name__)

    logg.info('hello')
    # print(logg.info('hello '))

    # threading.Thread(run(10)).start()
    # threading.Thread(run(20)).start()
    # threading.Thread(run(30)).start()
    # r1 = run(10)
    # r2 = run(20)
    # r1.send(None)
    # r2.send(None)




