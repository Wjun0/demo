import binascii
import sys
import os
import random,string
import time,requests
import datetime
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

basepath = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0,basepath)

from test_demo.log import Logger

import logging
logging.basicConfig(filename='sss.log',level=logging.INFO)


def github_test():
    key = "pab.com.cn"
    keyy2 = "pingan.com.cn"
    # 测试github 监控是否正常监控
    return

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
from apscheduler.triggers.cron import CronTrigger

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


def calculate_num(k):
    return k+1,k


def xss_filter(string):
    import bleach
    from bleach.sanitizer import ALLOWED_TAGS,ALLOWED_ATTRIBUTES
    print(string)
    new_content = bleach.clean(string,tags=ALLOWED_TAGS,attributes=ALLOWED_ATTRIBUTES)
    print("===============")
    print(new_content)


def jwt_test():
    data = {"username":"wangjun","name":"王军"}
    from itsdangerous import TimedJSONWebSignatureSerializer
    ser = TimedJSONWebSignatureSerializer("key",10)
    token = ser.dumps(data).decode()
    print(token)
    t = ser.loads(token.encode())
    print(t)

def pad_key(key):
    while len(key) % 16 != 0:
        key += b' '
    return key




if __name__ == '__main__':
    import sys


    res = requests.get("http://www.baidu.com")
    rest = requests.get("http://www.baidu.com",proxies={"http":"29.2.72.212:8080"})

    a = datetime.datetime.now().strftime("%Y-m-%dT%H:%M:%S.11Z")
    print(time.time())

    from Crypto.Cipher import AES
    import base64
    # key = "sdfssasdf"
    # sec = pad_key(key.encode())
    # obj = AES.new(sec, AES.MODE_CBC)
    # message = "The answer is no"
    # ciphertext = obj.encrypt(message.encode())
    # sign = str(base64.encodebytes(ciphertext),encoding='utf8').replace('\n','')
    # print(sign)

    secort = "sdfsdfasasssssss"
    data = {'name':"wangjun"}
    obj = AES.new(secort.encode(),AES.MODE_EAX,)
    ctext = obj.decrypt(pad_key(str(data).encode()))
    sign = str(base64.encodebytes(ctext),encoding='utf8').replace('\n','')
    print(sign)

    obj1 = AES.new(secort.encode(),AES.MODE_EAX, obj.nonce)
    d = obj.encrypt(sign.encode())
    print(d)

    jwt_test()

    str = "<script>xx<img/src/onerror=alert(/xss/)></script>"
    xss_filter(str)

    executor = ThreadPoolExecutor(max_workers=5)
    all_task = [executor.submit(calculate_num,i) for i in range(10)]
    wait(all_task,return_when=ALL_COMPLETED)
    for i in all_task:
        k,v = i.result()



    url = "http://cat.fat.com.cn/login1"
    from url_normalize import url_normalize
    new_url = url_normalize(url)

    key = binascii.hexlify(os.urandom(20)).decode()

    sc.add_job(ts, trigger=CronTrigger(minute=40,second=50))
    sc.start()






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

