#打印一个矩形
for i in range(1,5):
    if i == 1 or i == 4:
        for j in range(1,8):
            print('* ',end='')
    else:
        for m in range(1,8):
            if m == 1 or m == 7:
                print('* ',end='')
            else:
                print('  ',end='')
    print()
print('= '*20)
#打印菱形
for i in range(1,8):
    if i ==1 or i == 2 or i ==3 or i == 4:
        for j in range(1,5-i):
            print(' ',end='')
        for n in range(1,i+1):
            print('* ',end='')
    if  i == 5 or i == 6 or i == 7:
        for k in range(1,i-3):
            print(' ',end='')
        for v in range(1,9-i):
            print('* ',end='')
    print()
print('= '*20)
#打印直角三角形（靠左）
for i in range(1,6):
    for j in range(1,i+1):
        print('* ',end='')
    print()
print('= '*20)
#打印倒立直角三角性（靠左）
for i in range(1,6):
    for j in range(1,7-i):
        print('* ',end='')
    for n in range(1,i):
        print(' ',end='')
    print()
print('= '*20)
#打印倒立直角三角（靠右）
for i in range(1,6):
    for j in range(1,i):
        print('  ',end='')#这里少打一个空格就成了倒立的等边三角形
    for n in range(1,7-i):
        print('* ',end='')
    print()
print('= '*20)
#打印倒立的空直角三角形（靠右）
for i in range(1,6):
    for j in range(1,i):
        print('  ',end='')
    for n in range(1,7-i):
        if i == 1 or i == 5:
            print('* ',end='')
        elif n == 1 or n == 6-i:
            print('* ',end='')
        else:
            print('  ',end='')
    print()
print('= '*20)
#空心等边三角形（正立）
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end='')
    for n in range(1,1+i):
        if i == 1 or i == 5:
            print('* ',end='')
        elif n == 1 or n ==i:
            print('* ',end='')
        else:
            print('  ',end='')
    print()
print('= '*20)
#打印字母A
for i in range(1,7):
    for j in range(1,7-i):
        print(' ',end='')
    for n in range(1,1+i):
        if i == 1 or i == 4:
            print('* ',end='')
        elif n == 1 or n ==i:
            print('* ',end='')
        else:
            print('  ',end='')
    print()
print('= '*20)
#打印空心菱形
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end='')
    for m in range(1,1+i):
        if m == 1 or m == i:
            print('* ',end='')
        else:
            print('  ',end='')
    print()
for i1 in range(1,5):
    for j1 in range(1,1+i1):
        print(' ',end='')
    for m1 in range(1,6-i1):
        if m1 == 1 or m1 == 5-i1:
            print('* ',end='')
        else:
            print('  ',end='')
    print()
print('= '*20)
#打印实心梯形
for i in range(1,5):
    for j in range(1,5-i):
        print(' ',end='')
    for m in range(1,5+i):
        print('* ',end='')
    print()
print('= '*20)
#打印空心梯形
for i in range(1,5):
    for j in range(1,5-i):
        print(' ',end='')
    for m in range(1,5+i):
        if i == 1 or i == 4:
            print('* ',end='')
        elif m == 1 or m == 4+i:
            print('* ',end='')
        else:
            print('  ',end='')
    print()
print('= '*20)
#打印字母D
for i in range(1,3):
    for j in range(1,2+i):
        if j == 1 or j == 1+i:
            print('* ',end='')
        else:
            print('  ',end='')
    print()
for i1 in range(1,3):
    for j1 in range(1,5-i1):
        if j1 == 1 or j1 == 4-i1:
            print('* ',end='')
        else:
            print('  ',end='')
    print()
print('= '*20)
#打印字母R
for i in range(1,3):
    for j in range(1,2+i):
        if j == 1 or j == 1+i:
            print('* ',end='')
        else:
            print('  ',end='')
    print()
for i in range(1,4):
    for j in range(1,2+i):
        if j == 1 or j == 1+i:
            print('* ',end='')
        else:
            print('  ',end='')
    print()
print('= '*20)
#递归函数，要有递归关系和约束条件
def digui(num):
    print(2+num)
    if num > 0:
        #调用本身的函数
        digui(num-1)
    else:
        print('= '*20)
    print(num)#如果是在else语句下则只会打印一个0，要是不在则会按顺序把出现过所有的数字全部都打印出来
digui(4)
#汉诺塔递归函数
i = 0
def hanno(n,a,b,c):
    global i
    if n == 1:
        i = i + 1
        print('这是第{}步'.format(i),a+'- >'+c)
    else:
        print(1)
        hanno(n-1,a,c,b)
        print(2)
        hanno(1,a,b,c)
        print(3)
        hanno(n-1,b,a,c)
        print(4)
a = 'A'
b = 'B'
c = 'C'
hanno(3,a,b,c)
#四个不同数字能组成多少个数组
n = 0
for i in range(1,5):
    for j in range(1,5):
        for m in range(1,5):
            if i !=j or i !=m or j !=m:
                n += 1
                print('这是第{}个数'.format(str(n)),i,j,m)
#输入三个整数，把这三个整数由小到大排列出
def dx(x,y,z):
    l = []
    l.append(x)
    l.append(y)
    l.append(z)
    l.sort()
    print(l)
    return l
dx(5,6,4)
help(str())