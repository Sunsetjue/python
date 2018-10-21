import threading
import time
class MyThread(threading.Thread):
    def __init__(self,args):
        super(MyThread,self).__init__()
        self.args = args
    def run(self):
        #必须重写run函数，run函数代表的是真正执行的功能
        time.sleep(1)
        print('The args for this class is {},时间是{}'.format(self.args,time.ctime()))
for i in range(5):
    t = MyThread('233333')
    t.start()
print('this is down')