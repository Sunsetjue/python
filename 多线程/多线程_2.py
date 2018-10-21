import time
import threading
def func1():
    print('this is a funcation')
    print('now,time is:',time.ctime())
    time.sleep(4)
    print('I get up now')
print('233333')
t1 = threading.Thread(target=func1,args=())
t1.daemon = True#daemon表示支线程会随着主线程的结束而结束
#t1.setDaemon(True)
t1.start()
time.sleep(2)
print('this is end of code')
# 此案例中如果没有t1.daemon = True,那么func1中的'I get up now’则会打印出来
# 由于主线程的最后一句话'this is a end of code'已经执行，所以'I get up now'就不会再执行了