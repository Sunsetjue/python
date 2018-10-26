from collections import namedtuple

ResClass = namedtuple('Res','count average')

#子生成器
def average():
    total = 0.0
    count = 0
    average = None
    while True:
        item = yield
        if item is None:
            break
        total += item
        count += 1
        average = total / count
    return ResClass(count,average)
#委派生成器
def group(storages,key):
    while True:
        storages[key] = yield from average()

#客户端代码
def client():
    process_data = {
        'boys_2': [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
        'boys_1': [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46]
    }
    storages = {}
    for k,v in process_data.items():
        #获得协程
        s = group(storages,k)
        #预激协程
        next(s)
        for i in v:
            s.send(i)
        #终止协程
        s.send(None)
    print(storages)

client()
     
