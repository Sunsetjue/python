import threading
import time

class ThreadFunc():
    def __init__(self,name):
        self.name = name
    def thread(self,nloop,sec):#nloop表示要运行函数的名称，sec表示中间程序休息的时间
        print('Start loop',nloop,time.ctime())
        time.sleep(sec)
        print('Down loop',nloop,time.ctime())
def main():
    print('Start at:',time.ctime())
    t = ThreadFunc('loop')
    t1 = threading.Thread(target=t.thread,args=('1loop',4))
    t2 = threading.Thread(target=t.thread,args=('loop2',2))
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    print('All down at:',time.ctime())
if __name__ == '__main__':
    main()