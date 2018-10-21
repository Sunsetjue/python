#多进程派生子类的使用
import multiprocessing
from time import sleep,ctime
class Process(multiprocessing.Process):
    def __init__(self,sec):
        super(Process,self).__init__()
        self.sec = sec
        self.start()
    def run(self):
        while True:
            print('The time is',ctime())
            sleep(self.sec)
if __name__ == '__main__':
    Process(3)
    while True:
        print('Sleeping .......')
        sleep(1)
