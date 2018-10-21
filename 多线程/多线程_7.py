'''
生产者消费者问题

一个模型，可以用来搭建消息队列，
queue是一个用来存放变量的数据结构，特点是先进先出，内部元素排队，可以理解成一个特殊的list
'''

import threading
import time
import queue
#定义一个生产者的类，专门生产产品
class Producer(threading.Thread):
    def __init__(self):
        super(Producer,self).__init__()
        self.start()
    def run(self):
        global queue
        count = 0
        while True:
            #queue.qsize()返回queue的内容长度
            if queue.qsize()<20:
                for i in range(10):
                    count += 1
                    msg = '生成产品'+str(count)
                    #put是指向queue里放一个值
                    queue.put(msg)
                    print(msg)
                time.sleep(0.5)

#定义一个消费者的类
class Consumers(threading.Thread):
    def __init__(self):
        super(Consumers,self).__init__()
        self.start()
    def run(self):
        global queue
        while True:
            if queue.qsize()>10:
                for j in range(30):
                    msg = '消费了'+queue.get()
                    #queue.get()表示从queue中取出值
                    print(msg)
                time.sleep(1)

def main():
    for n in range(30):
        queue.put('初始化产品'+str(n))
    Producer()
    Consumers()

if __name__ == '__main__':
    queue = queue.Queue()
    main()


