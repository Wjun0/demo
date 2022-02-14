
from concurrent.futures import ThreadPoolExecutor,wait,ALL_COMPLETED
import requests


def task(url,i):
    data = requests.get(url)
    return data.text


def max_request_test():
    executor = ThreadPoolExecutor(max_workers=100)
    url = "http://192.168.59.139:8899/user/say/"
    all_task = [executor.submit(task,url,i) for i in range(1000)]

    wait(all_task,return_when=ALL_COMPLETED)
    for i in all_task:
        print(i.result())


if __name__ == '__main__':
    url = "http://192.168.59.139:8899/user/say/"
    res = requests.get(url)
    max_request_test()