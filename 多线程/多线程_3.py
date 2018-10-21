import time
import threading
def loop1():
    print('Start loop1 at:',time.ctime())
    time.sleep(4)
    print('End loop1 at:',time.ctime())

def loop2():
    print('Start loop2 at:',time.ctime())
    time.sleep(1)
    print("End loop2 at:",time.ctime())

def loop3():
    print('Start loop3 at:',time.ctime())
    time.sleep(3)
    print('End loop3 at:',time.ctime())

def main():
    print('Start at:',time.ctime())
    t1 = threading.Thread(target=loop1,args=())
    #setName是给每个子线程设置一个名字
    t1.setName('thread1')
    t1.start()

    t2 = threading.Thread(target=loop2,args=())
    t2.setName('thread2')
    t2.start()

    t3 = threading.Thread(target=loop3,args=())
    t3.setName('thread3')
    t3.start()

    #预计两秒后，loop2子线程已经运行结束
    time.sleep(2)
    for thr in threading.enumerate():
        print('正在运行着的线程的名称为:',thr.getName())

    print('正在运行着的线程的数量为:',len(threading.enumerate()))

    print('All down at:',time.ctime())

if __name__ == '__main__':
    main()