'''
线程替代方案
subprocess

完全跳过线程，使用进程
是派生进程的主要替代方案
python2.4后引入
multiprocessiong

使用threadiing借口派生，使用子进程
允许为多核或者多cpu派生进程，接口跟threading非常相似
python2.6
concurrent.futures

新的异步执行模块
任务级别的操作
python3.2后引入
'''

import multiprocessing
import time

def clock(sec):
    while True:
        print('The time is',time.ctime())
        time.sleep(sec)

if __name__ == '__main__':
    m = multiprocessing.Process(target=clock,args=(3,))#多进程，两个进程一起跑，互相不影响
    m.start()

    while True:
        print('Sleeping .......')
        time.sleep(1)