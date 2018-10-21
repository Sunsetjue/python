#多线程锁的概念，避免多个支线程占用同一个变量
import threading

lock = threading.Lock()
sum = 0
times = 100000
def addFunc():
    global sum,times,lock
    for i in range(times):
        lock.acquire()#将要进行的操作加上锁，等执行完这个再释放锁
        sum += 1
        lock.release()#释放锁
#上述函数表示将sum加上100000次1

def lessFunc():
    global sum,times,lock
    for j in range(times):#进行同样的获得锁和释放锁的操作
        lock.acquire()
        sum -= 1
        lock.release()

#再将sum减上100000次1

#运行函数
def main():
    print('Start at',sum)
    t1 = threading.Thread(target=addFunc,args=())
    t2 = threading.Thread(target=lessFunc,args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('Down at',sum)
#如果采用多线程，则会出现滥用sum,两个函数顺便使用。乱了套。因此需要采用锁的机制，每次只有一个支线程在用
if __name__ == '__main__':
    main()

