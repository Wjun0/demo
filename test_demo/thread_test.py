import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor,wait


def main(page):
    time.sleep(2)
    return page**2

def process_test():
    # 多进程
    t1 = time.time()
    with ProcessPoolExecutor(max_workers=10) as executor:
        all_task = [executor.submit(main,page) for page in range(100)]
        wait(all_task)
        for task in all_task:
            print(task.result())
    print("耗时：",time.time() -t1)


def thread_test():
    t1 = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        all_task = [executor.submit(main, page) for page in range(100)]
        wait(all_task)
        for task in all_task:
            print(task.result())
    print("耗时：", time.time()-t1)

def async_process_test():
    t1 = time.time()
    executor = ProcessPoolExecutor(max_workers=10)
    all_task = [executor.submit(main, page) for page in range(100)]
    # wait(all_task)       # 异步不等待直接就过
    print("耗时",time.time() - t1)
    return "res"


if __name__ == '__main__':

    dic = {'k1':"v1","k2":"v2","k3":"v3"}
    del dic['k2']
    print(dic)
    process_test()
    thread_test()
    res = async_process_test()
    print(res)