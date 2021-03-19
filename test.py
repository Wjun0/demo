import sys
import os
import random,string
import time,requests
import datetime

basepath = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0,basepath)

from log import Logger

import logging
logging.basicConfig(filename='sss.log')



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

if __name__ == '__main__':



    # sc.add_job(log_test, 'interval',seconds=10, next_run_time=datetime.datetime.now())
    # start_time = datetime.datetime.strptime('2021-02-02 14:20:00','%Y-%m-%d %H:%M:%S')
    # sc.add_job(ts, 'interval',seconds=10, next_run_time=start_time)
    # sc._logger = logging
    # sc.start()



    times = 5
    data = 1
    while times > 0:
        data = {'times':times}
        if times == 3:
            break
        times -=1
    print(data)


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


    # this dev
    # this is debug
    # debug ok
    # add debug

