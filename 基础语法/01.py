message='i love python'
print(message)
what_he_does='plays '
his_instrument='guitar'
his_name='Robert Johnson '
artist_intro=his_name+what_he_does+his_instrument
print(artist_intro)
num=1
string='1'
print(1+int(string))#字符串和整数的互换
words='word'*3
print(words)
words='a looooooooog word'
num=13
string='good!'
total=string*(len(words)-num)#字符串与数字相乘
print(total)
list=['jiangbaolong','pengkaiyi','liuyang','sunbin']#列表
print(len(list))
del list[-1]#删除列表元素
print(list)
list.append('songyue')#添加列表元素
print(list)
list.insert(2,'sunbin')#插入元素
print(list)
list.sort()#排列列表
print(list)
list.sort(reverse=True)#反着排序
print(list)
print(list.pop(1))#暂时拿出列表元素
print(list)
list.remove(list[0])
print(list)
print(sorted(list,reverse=True))
list_1=list[:]
list_1.append('sunbin')
print(list_1)
print('C:\some\name')
print(r'C\some\name')#r来否认\n
print('word')
word='Python'
word_1='J'+word[1:]
print(word_1)
word_2='sunbin'+word[-2:]
print(word_2)
a=['a','b','c']
n=['1','2','3']
x=[a,n]
print(x)
print(x[1])#选择列表元素并组合
print(x[1][1])#选择列表元素并检索
word='friends'
find_fiend=word[0]+word[2:5]+word[-2]#朋友里找恶魔
print(find_fiend)
number='1386-666-0006'
hide_number=number.replace(number[:9],"*"*4+' '+'*'*3+' ')#电话号码的遮盖
print(hide_number)
def weight_converter(g):#g与kg的换算
    return str(1/1000*g)+'kg'
print(weight_converter(342))
def Bevel_length(a,b):#直角的两边a,b
    return 'The right triangle third side\'s length is {}'.format((a**2+b**2)**(1/2))
print(Bevel_length(b=4,a=3))
def Trapezoidal_area(s,d,h):#梯形的上底s,下底d,高h
    return (s+d)*h*(1/2)
print(Trapezoidal_area(1,2,3))
print(Trapezoidal_area(3,2,1))
def trapezoid_area(base_up,base_down,height=3):
    return (1/2)*height*(base_up+base_down)
print(trapezoid_area(1,2))
print(trapezoid_area(3,2,height=1))
def censored_text_create(name,message):#定义函数的名称和参数
    desktop_path='C://Users/l/Desktop/'#open函数打开桌面路径
    full_path=desktop_path+name+'.txt'#取名字和合并字符串
    files=open(full_path,'w')#打开文件，'w'参数代表写入模式
    files.write(message)#写入传入的参数message
    files.close()#关闭文档
    print('Down')#提示执行完操作
def text_filter(word,censored_word='lame',changed_word='Awesome'):#如何过滤关键词
    return word.replace(censored_word,changed_word)
print(text_filter('Python is lame'))
print(text_filter('I\'am lame'))#记录有引号的字符串
def text_censored_create(name,message):#文字过滤函数
    text_clean=text_filter(message)
    censored_text_create(name,text_clean)#文字过滤器（合并函数）
fruits=['apple','cherry','orange','banana']
for fruit in fruits:#for表示循环
    print('I like eat '+fruit)
print('My favorite fruit is '+fruits[1])
for number in range(0,6):#range作为创造数值,进行循环
    print(number)
squares=[]
for value in range(0,6):
    square=value**2
    squares.append(square)
print(squares)
squares_1=[]
for value in range(0,11):
    squares_1.append(value**2)
print(squares_1)
square=[value**2 for value in range(0,12)]#更简单的表示
number=[]
for num in range(0,6):
    nums=num**3
    number.append(nums)#表示用range列表的方法一
print(number)
number_1=[]
for num_1 in range(0,6):#表示用range列表的方法二
    number_1.append(num_1**3)
print(number_1)
number_3=[num_3**3 for num_3 in range(0,6)]#表示用rang列表的方法三
print(number_3)
print(sum(number+squares_1))
number=(1,2,3,4,5)
print(number[1])
numbers=(1,2,3,4)
for number in numbers:
    print(number)
number=(5,10,15,20)
print(number[0])
number=(5,10,20,25)
print(number[-1])
cars=['audi','bmw','toyota','subaru']
for car in cars:
    if car=='bmw':#if条件句
        print(car.upper())
    else:#注意引号
        print(car.title())
favorite_food='cake'
if favorite_food !='cake':#感叹表示否认，如果最爱是食物不是蛋糕
    print('I like cake')
else:
    print('I don\'t like fruit')
answer=18
if answer !=18:
    print('You are wrong,try again')
else:
    print('You are right')
def question(answer):
    if answer==18:
        print('You are right,good')
    else:
        print('You are wrong,try again')
print(question(18))
print(question(122))
age=44
if age<4:
    price=0
elif age<18 and age>4:#if-elif-else，用elif来处理多个条件问题
    price=10
else:
    price=20
age=1
if age>40:
    price=40
elif age<=40 and age>18:
    price=20
elif age<=18 and age>4:
    price=10
elif age<=4 and age>0:
    price=0
print('your admission cost '+str(price)+'RMB')
list=['apple','cherry','orange']
point='I like eat'
if 'apple' in list:
    print(point+ 'apple')
if 'cherry' in list:
    print(point+'cherry')
if 'water' in list:
    print(point+'water')#water不在列表中，if语句最后的判断为False
print('\nI like eat fruits')
def account_login():
    password=input('Paasword')
    if password=='123456':
        print('Login success!')
    else:
        print('Wrong password or invalid input!')
        account_login()
def question_1():#定义函数，并不需要参数
    answer=input('Please write down your answer:')#使用input获得用户输入的字符串并储存在变量answer里
    if answer=='18':
        print('You are right. Good!')
    else:
        print('You are wrong.Try again!')
        question_1()#运行函数
list=['#*#*','123456']#创建一个列表
def account_login_1():#定义函数
    password=input('Password:')#将用户输入的字符串储存到变量password里
    password_1=password==list[-1]
    password_2=password==list[0]
    if password_1:
        print('Login success!')
    elif password_2:
        new_password=input('Please write down new password:')
        list.append(new_password)
        print('Your password has changed successfully!')#更改密码
        account_login_1()
    else:
        print('Wrong password or invalid input!')
        account_login_1()#在更改后再次使用函数，即再次让用户输入密码
for every_letter in "hello,world!":
    print(every_letter)
for num in range(1,11):
    print(str(num)+'+1 =',num+1)
songlist=['Holy Diver','Thunderstruck','Rebel Rebel']
for song in songlist:
    if song=='Holy Diver':
        print(song,'- Dio')
    elif song=='Thunderstruck':
        print(song,'- AC/DC')
    elif song=='Rebel Rebel':
        print(song,'- David Bowie')
for num_1 in range(1,10):
    for num_2 in range(1,10):
        print('{}X{}={}'.format(num_1,num_2,num_1*num_2))
count=0
while True:#while循环：只要条件成立，则会一直运行
    print('Repeat this line!')
    count=count+1
    if count==4:
        break#程序在上面条件成立的时候停下里
list=['00000','123456']
def login_in():
    count=0
    password=input('Password:')
    password_1=password==list[-1]
    password_2=password==list[0]
    if password_1:
        print('Login in success!')
    elif password_2:
        new_password=input('Please write down new password:')
        list.append(new_password)
        print('You has changed password successfully!')
        login_in()
    else:
        while True:
            print('Wrong password or invalid input!')
            count=count+1
            if count==3:
                print('You have write the wrong password three times,you can\'t write down again!')
                login_in()
password_list=['000','123456']
def account_login():
    tries=3
    while tries>0:#增加while循环，如果tries>0这个条件成立，那么便可以输入密码，从而执行辨别密码是否正确的逻辑判断
        password=input('Please write down password:')
        password_1=password==password_list[-1]
        password_2=password==password_list[0]

        if password_1:
            print('Login in!')
            break

        elif password_2:
            new_password=input('Please write down new password:')
            password_list.append(new_password)
            print('You has changed new password successfully!')
            account_login()
        else:
            print('Wrong password or invalid input!')
            tries=tries-1
            print(tries,'times left')

    else:#while循环的条件不成立，运行下面的程序
        print('Your account has been suspended')

account_login()#调用函数
def create_text():
    for name in range(1,11):
        with open('C://Users/l/Desktop/'+str(name)+'.txt','w')as text:
            text.write('Hello,world!')
            text.close()
def invest(principal_amount,years,interest_rate):
    for year in range(1,years+1):
        principal_amount=(1+interest_rate)*principal_amount
        print( 'year{}: ${}'.format(year,principal_amount))
print(invest(100,8,0.05))
number=102
while number>3:
    number=number-2
    print(number)
def even_print():
    for i in range(1,101):
        if i % 2==0:#百分号计算数是求余数的意思，另一个是格式化字符串的意思
            print(i)
even_print()
name=12414124
print(str(len(name)))