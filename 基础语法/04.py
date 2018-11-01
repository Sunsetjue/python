for i in range(4):
    if i==0 or i==3:
        for j in range(5):
            print('* ',end='')
    if i==1 or i==2:
        for p in range(5):
            if p==0 or p==4:
                print('* ',end='')
            else:
                print('  ',end='')
    print()
for i in range(0,10):
    for j in range(1,i+1):
        print('{}x{}={} '.format(j,i,i*j),end='')
    print()
for i in range(5):
    for j in range(i+1):
        print('* ',end='')
    print()
for i in range(5):
    if i == 0 or i == 4:
        for j in range(i+1):
            print('* ',end='')
    else:
        for m in range(i+1):
            if m==0 or m==i:
                print('* ',end='')
            else:
                print('  ',end='')
    print()
def hollow_triangle(m):
    for i in range(m):
        if i==0 or i==m-1:
            for j in range(i+1):
                print('* ',end='')
        else:
            for n in range(i+1):
                if n==0 or n==i:
                    print('* ',end='')
                else:
                    print('  ',end='')
        print()
print(hollow_triangle(8))
for i in range(5):
    if i==0 or i==4:
        for j in range(5-i):
            print('* ',end='')
    else:
        for j in range(5-i):
            if j==0 or j==4-i:
                print('* ',end='')
            else:
                print('  ',end='')
    print()
for i in range(5):
    for j in range(5-i):
        if i==0 or i==4:
            print('* ',end='')
        else:
            if j==0 or j==4-i:
                print('* ',end='')
            else:
                print('  ',end='')
    print()
for i in range(5):
    for j in range(5-i):
        print(' ',end='')
    for m in range(i+1):
        print('* ',end='')
    print()
for i in range(6):
    for j in range(6-i):
        print(' ',end='')
    for m in range(1+i):
        if m==0 or m==i or i==5:
            print('* ',end='')
        else:
            print('  ',end='')
    print()
for i in range(5):
    for j in range(1+i):
        if i==0 or i==4:
            print('* ',end='')
        else:
            if j==0 or j==i:
                print('* ',end='')
            else:
                print('  ',end='')
    print()
list=[1,2,3,4,5,6,9]
list1=list[:5]
print(list1)
print(id(list))
print(id(list1))
p='I love SongYue'
p1=p.title()#单词首字母大写，单词内大写变成小写
p2=p.upper()
p3=p.lower()
p4=p.capitalize()#首字母大写，其余全部小写
p5=p.swapcase()#大小写互换
print(p1,p2,p3,p4,p5)
o='dadasgfgdgerwer'
o1=o.find('d',3)
o2=o.find('d')#寻找字符串某个特定的位置
o3=o.index('r')#找不到会报错
o4=o.find('p')#找不到会显示-1
print(o1,o2,o3,o4)
print(o.count('d'))#寻找某特定字符串的出现次数
message='I like 孙彬'
message1=message.maketrans('孙彬','宋越')
print(message.translate(message1))
print(message1)
list1=[1,1,1,3,3,3,4,24,124,24,443,24,2,4234]
print(list1.count(3))#记录列表中某个字符或数字出现的次数
list2=['I love SunBin']
list3=['L love SongYue']
list4=list2.extend(list3)
print(list4)
print(list2+list3)
print(list2)
print(list1.index(2,4,13))#index后表示第一个是要找的值，第二个第三个是指开始和终止的地方，再找到第一个后就会停下来
print(list1.count(1))#记录列表元素出现的次数
help(list.count)
list=[1,2,3,4]
dict1={}.fromkeys(list,'sunbin')#按照指定的序列为键创建字典，值只有一个，都是一样的
print(dict1)
dict2={'a':1,'b':2,'c':3}
#寻找字典里键的值，没有不会报错，会返回None，在没有找到的情况下，如果有默认值，则返回默认值，没有就会返回None
print(dict2.get('a'))
print(dict2.get('d'))
print(dict2.get('d',4))
print(dict2.pop('c'))#移除指定的字典里的值和键
print(dict2)
print(dict2.popitem())#移除字典最后一个键和值
print(dict2)
dict2.setdefault('b',2)#添加字典的键和值
print(dict2)
dict2.update({'a':2,'b':1})#改变字典里的所有键和值
print(dict2)
a=set()
print(a)
list=[1,2,3,1,4,2,3]
a=set(list)
print(a)
set1=(1,3,3,3,2,2,1,4,3,1)
print(set1)
set2=set(set1)
print(set2)
set3={1,3,2,3,'a','b'}
set3.add(6)#add只能添加一个元素
print(set3)
set3.pop()#删除一个元素
print(set3)
set3.pop()
print(set3)
set3.remove('b')#删除指定的元素，如果没有就会报错
print(set3)
set3.discard(6)#也是删除指定元素，不过不会报错
print(set3)
set3.discard('c')
print(set3)
set4={1,3,4,5,5,7,6,'a','c','e'}
set5={1,2,3,4,5,6,7,7,9,'a','d','e'}
set6=set4.difference(set5)#差集，并不会改变原集合set4
set7=set5.difference(set4)
print(set6)
print(set7)
print(set4)
print(set5)
set8=set4.difference_update(set5)#差集，但会去掉原集合的与比较集合之间的交集，会改变原集合
print(set8)
print(set4)
print(set5)
#函数文档
def weight_converter(g):
    '''
    重量转换器
    :param g: 输入g
    :return: 得到kg
    '''
    return str(g*10000/1)+'kg'
print(help(weight_converter))
print(weight_converter.__doc__)#查看函数文档的两种办法
def stu( *args):
    print(type(args))
    for i in args:
        print(i)
stu('sunbin',24,'man')
def stu(name,age,hobby='None', *args, **kwargs):#收集参数混合函数实例
    '''
    学生自我介绍所需要说出的东西的函数
    :param name: 自己的名字
    :param age: 年龄
    :param hobby: 兴趣爱好，可以没有
    :param args: 自己还想要补充的东西
    :param kwargs: 与自己有关一一对应的东西
    :return: None
    '''
    print('my name is {},I\'m {} years old'.format(name,age))
    if hobby == 'None':
        print('I don\'t have hobby')
    else:
        print('My hobby is {}'.format(hobby))
    print('*'*23)
    print(type(args))#args用于收集函数内的所有参数，类似于列表，类型为tuple
    for i in args:
        print(i)
    print('*'*25)
    print(type(kwargs))#类似于字典
    for k,v in kwargs.items():
        print(k,'- - - ',v)
stu('sunbin',21,'man','single','like play games',father='yingengxin',mather='sunyuping',school='yingkouligongyueyuan')
x = 1
y = 2
z2 = x + y
z1 = eval('x+y')#把字符串转换成代码并返回结果
z3 = exec('x+y')#把字符串转换成代码但并部返回结果
print(z1)
print(z2)
print(z3)
def num():
    global b#把局部变量转换成全局变量
    b = 32
    print(b)
num()
print(b)
print('*'*10)
def fub(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n <= 0:
        n = int(input('请写出一个大于0的第n个数：'))
    return fub(n-1)+fub(n-2)
print(fub(10))
