import threading
import time

#死锁的解决办法2，使用信号灯
# 参数定义最多几个线程同时使用资源
semaphore = threading.Semaphore(3)

def func():
    if semaphore.acquire():
        for i in range(5):
            print(threading.currentThread().getName() + ' get semaphore')
        time.sleep(10)
        semaphore.release()
        print(threading.currentThread().getName() + ' release semaphore')


for i in range(8):
    t1 = threading.Thread(target=func)
    t1.start()