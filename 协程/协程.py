'''
可迭代(Iterable):直接作用于for循环的变量
迭代器(Iterator):不但可以作用于for循环，还可以被next调用
list是典型的可迭代对象，但不是迭代器
通过isinstance判断
'''
from collections import Iterable,Iterator
l1 = [1,2,3,4,5]
print(isinstance(l1,Iterable))#判断l1是否为可迭代的
print(isinstance(l1,Iterator))#判断l1是否为迭代器

#iter函数可以把可迭代转换为迭代器
msg = 'I love SongYue'
print(isinstance(msg,Iterable))
print(isinstance(msg,Iterator))

msg1 = iter(msg)
print(isinstance(msg1,Iterable))
print(isinstance(msg1,Iterator))


def func(n):
    t = 0
    a = 0
    b = 1
    while t < n :
        print(b)
        a,b = b,a+b
        t += 1
func(5)

'''
生成器
generator: 一边循环一边计算下一个元素的机制/算法
需要满足三个条件：
每次调用都生产出for循环需要的下一个元素或者
如果达到最后一个后，爆出StopIteration异常
可以被next函数调用
如何生成一个生成器
直接使用
如果函数中包含yield，则这个函数就叫生成器
next调用函数，遇到yield返回
'''
# 直接使用生成器

L = [x*x for x in range(5)] # 放在中括号中是列表生成器
g = (x*x for x in range(5))#  放在小括号中就是生成器

print(type(L))
print(type(g))

def step():
    print('Step 1')
    yield 1
    print('Step 2')
    yield 2
    print('Step 3')
    yield 3
    return None
s = step()#调用生成器
sc = next(s)#预激
print(sc)#执行yield前的命令，到达yield停止函数，然后返回yield后的值，如果没有则不返回

#for循环调用生成器
'''
def add(t):
    n,a,b = 0,0,1
    while t>n:
        yield b
        a,b = b,a+b
        n += 1
    return None
g = add(6)
for i in range(8):
    g2 = next(g)
    print(g2)
'''

'''
协程
历史历程
3.4引入协程，用yield实现
3.5引入协程语法
实现的协程比较好的包有asyncio, tornado, gevent
定义：协程 是为非抢占式多任务产生子程序的计算机程序组件，协程允许不同入口点在不同位置暂停或开始执行程序”。
从技术角度讲，协程就是一个你可以暂停执行的函数，或者干脆把协程理解成生成器
协程的实现：

yield返回
send调用
协程的四个状态

inspect.getgeneratorstate(…) 函数确定，该函数会返回下述字符串中的一个：
GEN_CREATED：等待开始执行
GEN_RUNNING：解释器正在执行
GEN_SUSPENED：在yield表达式处暂停
GEN_CLOSED：执行结束
next预激（prime)
协程终止

协程中未处理的异常会向上冒泡，传给 next 函数或 send 方法的调用方（即触发协程的对象）
止协程的一种方式：发送某个哨符值，让协程退出。内置的 None 和Ellipsis 等常量经常用作哨符值==。
yield from

调用协程为了得到返回值，协程必须正常终止
生成器正常终止会发出StopIteration异常，异常对象的vlaue属性保存返回值
yield from从内部捕获StopIteration异常
委派生成器
包含yield from表达式的生成器函数
委派生成器在yield from表达式出暂停，调用方可以直接把数据发给自生成器
子生成器在把产出的值发给调用放
自生成器在最后，解释器会抛出StopIteration，并且把返回值附加到异常对象上
'''
def simple_coroutine():
    print('>- Start')
    x = yield
    print('>-receive',x)
#主线程的调用
s = simple_coroutine()
s2 = next(s)#预激
print('*'*10)
#s.send('sunbin')#调用

def simple_coroutine2(w):
    print('-> Start')
    x = yield w
    print('-> receive',w,x)
    y = yield x+w
    print('-> receive',w,x,y)
    z = yield w+x+y
    print('-> receive',w,x,y,z)
l = simple_coroutine2(1)
l1 = next(l)
print(l1)
l2 = l.send(2)
print(l2)
l3 = l.send(3)
print(l3)
l4 = l.send(4)
print(l4)