import threading
import time

def func():
    print("I am running.........")
    time.sleep(4)
    print("I am done......")



if __name__ == "__main__":
    i = 0
    t = threading.Timer(6, func)# Timer后的参数表示几秒后运行后面的函数
    t.start()

    while True:
        print("{0}***************".format(i))
        time.sleep(3)
        i += 1