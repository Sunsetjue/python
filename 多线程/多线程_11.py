# 有关多进程的消费者和生产者的关系，queue
import multiprocessing
import time

def consumer(input_q):
    print('Into consumer:',time.ctime())
    while True:
        item = input_q.get()
        if item is None:#设置哨兵
            break
        print('pull',item,'out of q')
    print("Out of consumer:",time.ctime())

def producer(sequence, output_q):
    print ("Into producer:", time.ctime())
    for item in sequence:
        output_q.put(item)
        print ("put", item, "into q")
    print ("Out of producer:", time.ctime())

if __name__ == '__main__':
    q = multiprocessing.Queue()
    m = multiprocessing.Process(target=consumer,args=(q,))
    m.daemon = True
    m.start()
    sequence = [1,2,3,4]
    producer(sequence,q)

    q.put(None)
    m.join()