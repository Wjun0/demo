import binascii
import sys
import os
import random,string
import time,requests
import datetime
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

basepath = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0,basepath)

from log import Logger

import logging
logging.basicConfig(filename='sss.log',level=logging.INFO)



def random_key(length=20):
    return "".join(
        (
            random.choice(
                random.choice(
                    (
                        string.ascii_uppercase,
                        string.ascii_lowercase,
                        "".join(map(str, range(0, 9))),
                    )
                )
            )
            for _ in range(1, length)
        )
    )


class A():
    def run(self):
        print('start')


from apscheduler.schedulers.background import BlockingScheduler
sc = BlockingScheduler()


def run():
    try:
        A().run()

    except Exception as e:
        print(e)
        import sys
        sys.exit()
    print('ok')

# sc.add_job(run, 'cron', hour='9',minute='48',second='0')
# sc.add_job(run, 'interval',seconds=10)

def log_test():

    info_log = Logger('in.log', level='info')
    error_log = Logger('er.log', level='error')

    info_log.logger.info('1111')
    info_log.logger.info('2222')
    error_log.logger.error('eeeee')
    error_log.logger.error('rrrrr')

def ts():
    print('hello ')

def ppp(i):
    # r = random.randint(4,5)
    time.sleep(1)
    i +=1
    print(i)
    return {"i": i}



def apschedul(i):
    print(i)
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.bind(("127.0.0.1",8888))
    except socket.error:
        print("scheduler is running")
    else:
        print("start scheduler")
    time.sleep(10)





if __name__ == '__main__':
    key = binascii.hexlify(os.urandom(20)).decode()


    q = 0/1
    print(q)
    s1 = {1,2,3}
    s2 = {2,3,4}
    s1 = s1 | s2

    list1 = [111,22]
    l = list1.extend([333])
    print(l)
    t1 = "2021-03-03 12:12:12"
    t2 = "2021-03-03 13:12:12"
    t11 = datetime.datetime.strptime(t1,"%Y-%m-%d %H:%M:%S")
    t22 = datetime.datetime.strptime(t2,"%Y-%m-%d %H:%M:%S")
    d = (t22-t11).total_seconds()
    import datetime
    d = datetime.datetime.now().isoweekday()
    if d not in [6,7]:
        print(d)
    print(datetime.datetime.now())

    import socket
    from concurrent.futures import ThreadPoolExecutor
    executor = ThreadPoolExecutor(max_workers=5)
    all_task = [executor.submit(apschedul,i) for i in range(10)]
    time.sleep(10)
    print("==")






    # print(datetime.datetime.now())
    # start = time.time()
    # executor = ThreadPoolExecutor(max_workers=20)
    # all_task = [executor.submit(ppp,i) for i in range(100)]
    # wait(all_task, return_when=ALL_COMPLETED)
    # for i in all_task:
    #     print(i)
    #     print(i._result)
    # print(f"耗时:{time.time()-start}")
    # print(all_task)

    # print(high,w,low)
    # sc.add_job(log_test, 'interval',seconds=10, next_run_time=datetime.datetime.now())
    # start_time = datetime.datetime.strptime('2021-02-02 14:20:00','%Y-%m-%d %H:%M:%S')
    # sc.add_job(ts, 'interval',seconds=10, next_run_time=start_time)
    # sc.add_job(ts, 'interval',seconds=10, next_run_time=datetime.datetime.now())
    # sc._logger = logging
    # sc.start()



    # times = 5
    # data = 1
    # while times > 0:
    #     data = {'times':times}
    #     if times == 3:
    #         break
    #     times -=1
    # print(data)


    # user = random.choice(['sadf','skdjf23','sdf23rdsf'])
    # pwd = 'xsadfass'
    # print(user)
    # with open('user.txt','a')as f:
    #     f.write(user + '  ' + pwd + '\n')

    # with open('user.txt','r')as f:
    #     lis = f.readlines()
    #     for i in lis:
    #         item = i.split('  ')
    #         print(item[0])
    #         print(item[1])

    # data = random_key(random.randint(5,20))
    # print(data)
    # TestDecorate().main()
    # try:
    #     sc.start()
    # except:
    #     sc.shutdown()

    # log = Logger('all_log',level='debug')
    # log.logger.error('error')
    # log.logger.info('info')
    # data = requests.get('http://47.75.171.136:9000/dock_data/spiderinfo/')
    # dic = data.json()
    # print(dic)
    # dic1 = {'id':1,'name':'wj'}
    # dic2 = {'name':'wj','id':1}
    # if dic1 == dic2:
    #     print('==')
    # else:
    #     print('!=')

    ##



    # this dev
    # this is debug
    # debug ok
    # add debug

