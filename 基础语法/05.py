#汉诺塔方程
def hanno(n,a,b,c):
    if n == 1:
        print(a,' -> ',c)
        return None
    if n == 2:
        print(a,' -> ',b)
        print(a,' -> ',c)
        print(b,' -> ',c)
        return None
    '''
    当n=n 时候，把 n-1 个盘子从 a 借助于 c 运到 b 上，然后将 a 盘上的一个运到 c 塔上
    然后将 b 塔上的 n-1 个盘子通过 a 塔运送到 c 塔上
    '''
    hanno(n-1,a,c,b)
    print(a,' -> ',c)
    hanno(n-1,b,a,c)
a = 'A'
b = 'B'
c = 'C'
n = 3
hanno(n,a,b,c)
#列表内涵 list content. 创建一个和一个列表相同的列表,创建的列表为新列表，不与原来的相同
list1 = [1,2,3,4,5]
list2 = [i for i in list1]#对于原来所有的元素再重新赋值给新的列表
print(list2)
list3 = list1
print(id(list1))
print(id(list2))
print(id(list3))
#取 a 列表里面所有的偶数来生成 b 列表，再将 b 里面的元素打印出两倍的结果
a = [i for i in range(0,51)]
b = [j*2 for j in a if j % 2 == 0]#判断语句跟在后面,运算再跟在前面
print(b)
a = '1 2 3 4 4'
print(list(a))
b = 'I love SongYue'
print(list(b))#list函数的使用
a = [1,2,'sunbin',321]
b = a[0:2]
print(a)
print(id(a))#切片会改变生成新的列表，与原列表的的地址不同
print(b)
print(id(b))
# extend 函数是指将两个函数拼接在一起，但地址并不会变,还是原来拼的第一个列表
a = [1,2,3,4,5]
b = [6,7,8,9]
c = a+b#地址这样就发生了变化
print(c)
print(id(a))
print(id(b))
print(id(c))
a.extend(b)
print(id(a))
print(a)
# count表示查找列表里面谋个元素出现的次数
a.append(8)
a.insert(2,8)
print(a.count(8))#表示a列表里面计出8所出现的次数
print(a)
a=b#简单的赋值操作会传地址
b[3] = 40
print(a)
print(id(a))
print(id(b))
#使用 a=b 简单赋值操作会传地址导致b改变使得a也随之改变，因此需要使用copy 函数
c=a.copy()#copy 函数的使用方法
c[3] = 43
print(a)
print(c)#此时a 和 c所打印出来的元素便不一样了，地址也不同
t = (1,1,3,4,5,6,100,100,7,8,89,89,102,0,3,105,105,23)
print(min(t))
print(max(t))
#元组变量的转换
a=1
b=2
print(a,b)
a,b=b,a
print(a,b)
'''
- 集合内数据无序，无法使用索引和分片
- 集合内索引具有唯一性，可以排除重复数据
- 集合用花括号表示，但如果里面没有任何东西，则会默认表示为字典dict
'''
set=set(t)
print(set)
s1={(1,2,3),('sunbin','songyue','sunyuping'),(8,9,10)}#复合集合内容用循环表示出来
for i,j,l in s1:
    print(i,'- -',j,'- -',l)
for m in s1:
    print(m)
a = {1,2,3,4,5,1,6,2}
b = {2,3,451,3,1,321,31,2}
c = a.union(b)#union表示并集
print(c)
d = a.difference(b)#difference 表示差集
print(d)
e = a.intersection(b)#intersection表示交集
print(e)