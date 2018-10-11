import math
# celi()向上取整的操作
print(math.ceil(5.62))
print(math.ceil(5.01))
# floor()向下取整的操作
print(math.floor(5.62))
print(math.floor(5.01))
#查看系统保留的关键字，命名的时候不能用来当作变量
import keyword
print(keyword.kwlist)
#Pycharm内置的四舍五入的函数round()
print(round(5.01))
print(round(5.62))
#sqrt()开平方运算，返回浮点数，调用math
print(math.sqrt(9))
#pow()幂函数运算，返回浮点数，调用math.前一个数为被幂的值，第二个为指数
print(math.pow(2,8))
# fabs()对于一个数值获取绝对值,返回浮点值，调用math模块
print(math.fabs(-23))
print(math.fabs(23))
print(math.fabs(0))
#abs()也是对一个数值获取绝对值，返回一个整数，Pycharm自带的函数
print(abs(-23))
print(abs(23))
print(abs(0))
#modf()对一个浮点数的整数部分和小数部分拆开分成两部分,返回元组，小数部分在前
print(math.modf(8.4))
print(math.modf(-4))
#copysign()把后一个数的正负号传递给第一个数,返回浮点值，运用math模块
print(math.copysign(2,-1))
print(math.copysign(-3,-2))
print(math.copysign(2,0))
print(math.e)
print(math.pi)
print('= '*20)
import random
#random()表示从0到1 的随机数字，包括0但不包括1
for i in range(5):
    print(random.random())
print('= '*20)
for j in range(5):
    #randrange表示随机打印范围内的值，可以重复，不包括尾,可以指定间隔
    print(random.randrange(1,10))
    #randint随机给定范围内值的顺序，包括开头不包括结尾
    #  print(random.randint(1,10))
print('= '*20)
for m in range(5):
    print(random.randrange(1,6,2))#指定间隔后就只剩下1，3，5
print('= '*20)
# choice()随机获取列表中的一个值
l = [1,2,3,4,5,6,7]
print(random.choice(l))
# shuffle()随机打乱序列,打印返回值是None
l1 = [2,3,4,5,6,7,8]
random.shuffle(l1)
print(l1)#此时已经打乱了原来l1的顺序
print('= '*20)
# uniform（）表示打印范围内的随机数，包括小数
for n in range(5):
    print(random.uniform(1,5))

#输入一个三位数，如果它大于系统给的随机数，则减去随机数，如果小于随机数，则两者相加
'''
while 1:
    p = input('请输入一个三位数：')
    if p.isdigit() and 100 <= int(p) <= 999:
        print('- - - - -结束请输入-1- - - - -')
        o = random.randrange(100,1000)
        print('随机数为',o)
        if int(p) > o:
            p1 = int(p)-o
        else:
            p1 = int(p)+o
        print(p1)
    elif int(p) == -1:
        break
    else:
        print('请输入正确的数字')
'''
print('= '*20)


class Person():
    name = 'sunbin'#公共的变量(public)
    _age = 21#受保护的变量(protected)
    __gander = 'mam'#私人的变量(privated)
    def work(self):
        print('混吃等死')
class Student(Person):#继承父类的变量和函数
    def Do_things(self):
        print('do homework every day')
    def work(self):
        # super()代表父类
        super().work()
        self.Do_things()
    name = 'sunyuping'
print(Person.__mro__)
print(Student.__mro__)#__mro__表示打印出此类的所有父类
s = Student()
print(s._age)
print(s.work())
print(s.name)
#类里面的构造函数
class Teacher():
    def __init__(self):#__init__就是构造函数
        print('take class and make money')
Yang = Teacher()#会自动执行构造函数
print('= '*20)
class Student(Teacher):
    pass
    '''
    def __init__(self):
        print('pay for learn some acknowledge')
    '''
sunbin = Student()#子类没有构造函数则会自动向父类寻找构造函数，如果子类有函数，则会优先使用子类的构造函数
class A():
    def __init__(self):
        self.name = 'NoName'
        self.age = 21
        self.gender = 'man'
        print('我是一个学生')
class B(A):
    pass
b = B()
print(b.name)
print(b.age)
print(b.gender)
b.name = 'SongYue'
b.age = 15
b.gender = 'girl'
b.hobby = 'play'
print(b.name)
print(b.age)
print(b.gender)
print(b.hobby)
print('= '*20)
#构造函数和父类子类结合的例子
'''
class C():
    def __init__(self,name):
        print('My name is',name)
class D(C):
    def __init__(self,name,age):
        C.__init__(self,name)
        print('I\'am {} years old'.format(age))
class E(D):
    def __init__(self,name,age,gender):
        D.__init__(self,name,age)
        print('I\'am a',gender)
student1 = E('Sunbin',21,'boy')#输入姓名年龄和性别，自动打印出基本属性
'''
class C():
    def __init__(self,name):
        print('My name is',name)
class D(C):
    def __init__(self,name,age):
        super(D,self).__init__(name)#使用 super()函数的例子，括号里接的子类也就是本身，后面构造函数内没有self
        print('I\'am {} years old'.format(age))
class E(D):
    def __init__(self,name,age,gender):
        super(E,self).__init__(name,age)#__init__后接上变量，并没有self
        print('I\'am a',gender)
student2 = E('Sunbin',21,'boy')
# issubclass用于检测前面的是不是后面的子类  isinstance用于检测是否是类的实例
class A():
    pass
class B(A):
    pass
class C():
    pass
b = B()
print(isinstance(b,B))
print(issubclass(B,B))
print(issubclass(B,A))
print(issubclass(A,B))
print(issubclass(C,B))#返回一个布尔值
print(issubclass(C,object))#在Python里面所有类都是object的子类，一定返回True
help(setattr)
# 在用户输入年龄的时候，可以输入整数，小数，浮点数
# 但为了数据清洁，我们统一需要保留整数，直接舍去小数点
class P():
    def __init__(self):
        print('23333')
    def __call__(self):#函数当实例调用，自动调用
        print('322222')
    def __str__(self):#
        print('111111')
        return '2222'
    def __getattr__(self, age):#当实例没有时候，自动调用此函数
        print('3333')
        #return '333333'
    def __setattr__(self, key, value):# 将给定对象上的命名属性设置为指定的值。
        print('今天是',str(value))
        print(key)
        super().__setattr__(key,value)
p = P()
p()
print(p)
print(p.name)#类里面并没有name这个属性，因此调用__getattr__函数
p.date = 10.01
print('= '*20)
class People():
    def __init__(self,name):
        self.name = name
    def __gt__(self, other):# 进行大于判断的时候触发的函数
        print('哈哈,{}会比{}大吗'.format(self.name,other.name))
        return self.name > other.name
people1 = People('one')
people2 = People('two')
print(people2 > people1)
print('= '*20)
#类和对象的三种方法
# 1. 实例方法
# 2， 类方法
# 3. 静态方法
class A():
    def eat(self):#实例方法
        print(self)
        print('Eating.....')
    @classmethod#类方法
    def sleep(cls):
        print(cls)
        print('Sleeping....')
    @staticmethod#静态方法
    def sit():
        print('Sitting')
sunbin = A()
sunbin.eat()
A.sleep()
sunbin.sleep()
A.sit()
print('= '*20)
print('\n')

#ASCII字母转换成数字
#32～126(共95个)是字符(32是空格），其中48～57为0到9十个阿拉伯数字。
#65～90为26个大写英文字母，97～122号为26个小写英文字母，其余为一些标点符号、运算符号等。
print(ord('A'))
print(ord('a'))
#数字转化成字母
print(chr(100),'\n')

class A():
    def __init__(self):
        self.name = 'A'
    def fget(self):
        print('Aa')
        return self.name
    def fset(self,name):
        print(ord(self.name))
    def fdel(self):
        pass
    name2 = property(fget,fset,fdel,'对名字进行操作')
a = A()
print(a.name)
print(a.name2)
import tkinter
help(tkinter.create_oval)