import calendar
# calendar：　获取一年的日历字符串
# 参数
# w = 每个日期之间的间隔字符数
# l = 每周所占用的行数
# c = 每个月之间的间隔字符数
cal = calendar.calendar(2108)
print(cal)
cal = calendar.calendar(2018,w=4,l=1,c=5)
print(cal)
# isleap 判断某年是否为闰年
print(calendar.isleap(2018))#2018年不是闰年
print(calendar.isleap(2000))#2000年为闰年
# leapdays 表示某个区间年份的闰年个数
print(calendar.leapdays(1997,2018))
# monthrang 表示获取某个月是从周几开始并且这个月有多少天
i = calendar.monthrange(2018,10)
print(i)#返回的第一个数是从零开始的，即0表示星期一，6表示星期天
# monthcalendar 表示返回一个月每天的矩阵列表
i = calendar.monthcalendar(2018,10)
print(i)
print(calendar.month(2018,10))
print(calendar.weekday(2018,10,12))#也是0代表星期一，获取某年某月某日是周几
import time
'''
time模块
时间戳
- 一个时间表示，根据不同语言，可以是整数或者浮点数
- 是从1970年1月1日0时0分0秒到现在经历的秒数
- 如果表示的时间是1970年以前或者太遥远的未来，可能出现异常
- 32位操作系统能够支持到2038年

UTC时间
- UTC又称为世界协调时间，以英国的格林尼治天文所在地区的时间作为参考的时间，也叫做世界标准时间。
- 中国时间是 UTC+8 东八区

夏令时
- 夏令时就是在夏天的时候将时间调快一小时，本意是督促大家早睡早起节省蜡烛！ 每天变成25个小时，本质没变还是24小时

时间元组
- 一个包含时间内容的普通元组


    索引      内容    属性            值

    0       年       tm_year     2015
    1       月       tm_mon      1～12
    2       日       tm_mday     1～31
    3       时       tm_hour     0～23
    4       分       tm_min      0～59
    5       秒       tm_sec      0～61  60表示闰秒  61保留值
    6       周几     tm_wday     0～6
    7       第几天   tm_yday     1～366
    8       夏令时   tm_isdst    0，1，-1（表示夏令时）
'''
print(time.time())#显示时间戳
t = time.localtime()#显示当前的时间，包括索引的全部内容
print(t)
print(t.tm_min)#也可以显示部分的内容
tt = time.asctime(t)#显示时间，返回字符串内容（更方便观看）
print(tt)
t = time.ctime()#获取当前字符串时间
print(t)
# strftime:将时间元组转化为自定义的字符串格式
'''
格式  含义  备注
%a  本地（locale）简化星期名称    
%A  本地完整星期名称    
%b  本地简化月份名称    
%B  本地完整月份名称    
%c  本地相应的日期和时间表示    
%d  一个月中的第几天（01 - 31）   
%H  一天中的第几个小时（24 小时制，00 - 23）   
%I  一天中的第几个小时（12 小时制，01 - 12）   
%j  一年中的第几天（001 - 366）  
%m  月份（01 - 12） 
%M  分钟数（00 - 59）    
%p  本地 am 或者 pm 的相应符    注1
%S  秒（01 - 61）  注2
%U  一年中的星期数（00 - 53 星期天是一个星期的开始）第一个星期天之前的所有天数都放在第 0 周   注3
%w  一个星期中的第几天（0 - 6，0 是星期天） 注3
%W  和 %U 基本相同，不同的是 %W 以星期一为一个星期的开始  
%x  本地相应日期  
%X  本地相应时间  
%y  去掉世纪的年份（00 - 99）    
%Y  完整的年份   
%z  用 +HHMM 或 -HHMM 表示距离格林威治的时区偏移（H 代表十进制的小时数，M 代表十进制的分钟数）      
%%  %号本身
'''
t = time.localtime()
ft = time.strftime("%Y %m %d %H:%M",t)
print(ft)
# sleep表示使程序进入睡眠，n秒后继续
'''
datetime模块
datetime提供日期和时间的运算和表示
datetime.date 提供一个理想的日期，提供，year,month,day 属性
'''
import datetime
dt = datetime.datetime(2018,10,13)
print(dt)
print(dt.day)
print(dt.month)
print(dt.year)
# datetime.time: 提供一个理想和的时间， 居于哦hour， minute，sec，microsec等内容
# datetime.datetime: 提供日期跟时间的组合
# datetime.timedelta: 提供一个时间差，时间长度


# datetime.datetime
from datetime import datetime
# 常用类方法：
# today：
# now
# utcnow
# fromtimestamp： 从时间戳中返回本地时间
dt = datetime(2018,10,14)
print(dt.today())
print(dt.now())
print(dt.fromtimestamp(time.time()))
# datetime.timedelta表示一个时间间隔
from datetime import datetime,timedelta
dt = datetime.now()
td = timedelta(days=1)
print((dt+td).strftime('%Y-%m-%d %H:%M:%S'))
# timeit 时间测量工具
import timeit
c ='''
list = []
for i in range(10000):
    list.append(i)'''

#利用timeit函数调用代码，执行10000次，看需要运行多长时间
'''
t1 = timeit.timeit(stmt='[j for j in range(10000)]',number=10000)
t2 = timeit.timeit(stmt=c,number=10000)
print(t1)
print(t2)
'''
#在有函数变量的时候
d = '''
def message(num):
    list = []
    for i in range(num):
        print('repeat by {} times'.format(i))
        list.append(i)
        print(list)
'''
t3 = timeit.timeit('message(num)',setup=d+'num=3',number=5)
#print(t3)
'''
os - 操作系统相关
跟操作系统相关，主要是文件操作
于系统相关的操作，主要包含在三个模块里
os， 操作系统目录相关
os.path, 系统路径相关操作
shutil， 高级文件操作，目录树的操作，文件赋值，删除，移动
路径：
绝对路径： 总是从根目录上开始
相对路径： 基本以当前环境为开始的一个相对的地方
'''
import os
# getcwd()表示查看当前目录
print(os.getcwd())
# chdir()表示改变当前目录
os.chdir('C:\\Users\\l\\PycharmProjects')
print(os.getcwd())
os.chdir('C:\\Users\\l\\PycharmProjects\\sunbin_1')
print(os.getcwd())
# listdir()获取一个目录中所有子目录和文件的名称列表
print(os.listdir('C:\\Users\\l\\PycharmProjects\\sunbin_1'))
#mkdir()  创建文件夹
#os.mkdir('girls')
#os.mkdir('boys',0o777)

#makedirs()  递归创建文件夹
#os.makedirs('/home/sy/a/b/c/d')
#rename() 文件或文件夹重命名
#os.rename('/home/sy/a','/home/sy/alibaba'
#os.rename('02.txt','002.txt')
print('*'*20)
#os.system()执行系统命令
print(os.system('ls'))
#getenv() 获取指定的系统环境变量值
# 相应的还有putenv
#  格式：os.getenv('环境变量名')
#  返回值：指定环境变量名对应的值
rst = os.getenv("PATH")
print(rst)
'''
os.curdir: curretn dir,当前目录
os.pardir: parent dir， 父亲目录
os.sep: 当前系统的路径分隔符
windows: "\"
linux: "/"
os.linesep: 当前系统的换行符号
windows: "\r\n"
unix,linux,macos: "\n"
os.name： 当前系统名称
windows： nt
mac，unix，linux： posix
'''
print(os.curdir)
print(os.pardir)
print(os.sep)
print(os.linesep)
print(os.name)
'''
os.path 模块， 跟路径相关的模块
abspath() 将路径转化为绝对路径
abselute 绝对
 格式:os.path.abspath('路径')
返回值：路径的绝对路径形式

linux中
 . 点号，代表当前目录
 . . 双点，代表父目录
 
basename() 获取路径中的文件名部分
格式:os.path.basename(路径)
返回值：文件名字符串

join() 将多个路径拼合成一个路径
格式：os.path.join(路径1，路径2....)
返回值：组合之后的新路径字符串

split() 将路径切割为文件夹部分和当前文件部分
格式:os.path.split（路径）
返回值：路径和文件名组成的元组

isdir（） 检测是否是目录
格式：os.path.isdir(路径)
返回值：布尔值

exists() 检测文件或者目录是否存在
格式：os.path.exists(路径)
返回值:布尔值
'''
# shutil模块
# copy() 复制文件
#  格式：shutil.copy(来源路径，目标路径)
#  返回值：返回目标路径
# 拷贝的同时，可以给文件重命名

# copy2() 复制文件，保留元数据（文件信息）
#  格式：shutil.copy2(来源路径，目标路径)
#  返回值：返回目标路径
#  注意：copy和copy2的唯一区别在于copy2复制文件时尽量保留元数据

# copyfile()将一个文件中的内容复制到另外一个文件当中
#  格式：shutil.copyfile（'源路径','目标路径')
#  返回值：无

# move() 移动文件/文件夹
#  格式：shutil.move(源路径，目标路径)
#  返回值：目标路径！
list1 = [i for i in range(5)]
def cfa(n):
    return n * 10
list2 = map(cfa,list1)
for j in list2:
    print(j)
'''
系统高阶函数-map
原意就是映射，即把集合或者列表的元素，每一个元素都按照一定规则进行操作，生成一个新的列表或者集合
map函数是系统提供的具有映射功能的函数，返回值是一个迭代对象
reduce
原意是归并，缩减
把一个可迭代对象最后归并成一个结果
对于作为参数的函数要求： 必须由两个参数，必须由返回结果
reduce([1,2,3,4,5]) == f( f(f(f(1,2),3), 4),5)
reduce 需要导入functools包
'''
from functools import reduce
def jfa(x,y):
    return x + y
l = reduce(jfa,[i for i in range(1,20)])
print(l)
