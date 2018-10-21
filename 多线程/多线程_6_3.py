import threading
import time

#死锁问题的解决办法1
#在等待时间结束后，直接强行释放，让给另一个子线程

lock1 = threading.Lock()
lock2 = threading.Lock()
def func_1():
    print('func_1 starting .......')
    lock1.acquire(timeout=4)
    print('func_1申请了lock1 .......')
    time.sleep(2)
    print('func_1等待lock2 .......')

    rst = lock2.acquire(timeout=2)#这里表示申请lock2如果超过两秒还没有申请到，那么直接放弃申请进行下一步的操作
    if rst:
        print('func_1申请了lock2 ....')
        lock2.release()
        print('func_1释放了lock2 .....')
    else:
        print('func_1压根就没有申请到lock2')

    lock1.release()
    print('func_1释放了lock1 ......')

    print('func_1 down')

def func_2():
   print("func_2 starting.........")
   lock2.acquire()
   print("func_2 申请了 lock2....")
   time.sleep(4)
   print("func_2 等待 lock1.......")
   lock1.acquire()
   print("func_2 申请了 lock1.......")

   lock1.release()
   print("func_2 释放了 lock1")

   lock2.release()
   print("func_2 释放了 lock2")

   print("func_2 done..........")

if __name__ == '__main__':
    print("主程序启动..............")
    t1 = threading.Thread(target=func_1, args=())
    t2 = threading.Thread(target=func_2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("主程序结束..............")