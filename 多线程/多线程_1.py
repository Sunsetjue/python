import time
import threading
def loop1(para):
    print('loop1 start time:',time.ctime())
    print('这是{}写的参数'.format(para))
    time.sleep(4)
    print('loop1 end time:',time.ctime())

def loop2(para1,para2):
    print('loop2 start time:',time.ctime())
    print('这分别是{}和{}一起写的参数'.format(para1,para2))
    time.sleep(2)
    print('loop2 end time:',time.ctime())

def main():
    print('Start at', time.ctime())
    t1 = threading.Thread(target=loop1,args=('孙彬',))
    t1.start()
    t2 = threading.Thread(target=loop2,args=('孙彬','宋越'))
    t2.start()

    t1.join()#join()表示在这个之后的函数应该等线程做完后在执行主线程
    t2.join()

    print('Ending time:', time.ctime())

if __name__ == '__main__':
    main()