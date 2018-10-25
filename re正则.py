'''
正则表达式(RegularExpression, re)
是一个计算机科学的概念
用于使用单个字符串来描述，匹配符合某个规则的字符串
常常用来检索，替换某些模式的文本
正则的写法
.(点号):表示任意一个字符，除了\n, 比如查找所有的一个字符 .

[]: 匹配中括号中列举的任意字符，比如[L,Y,0] , LLY, Y0,

\d: 任意一个数字

\D:除了数字都可以

\s:表示空格，tab键

\S:除了空白符号

\w: 单词字符， 就是a-z, A-Z, 0-9, _

\W: 除了

*： 表示前面内容重复零次或者多次， \w

+: 表示前面内容至少出现一次

？： 前面才出现的内容零次或者一次

{m,n}:允许前面内容出现最少m次，最多n次

^:匹配字符串的开始

$:匹配字符串的结尾

\b:匹配单词的边界

():对正则表达式内容进行分组， 从第一个括号开始，编号逐渐增大

  验证一个数字： ^\d$
  必须有一个数字，最少一位：^\d+$
  只能出现数字，且位数为5-10位： ^\d{5,10}$
  注册者输入年龄，要求16岁以上，99岁以下： ^[16-99]$
  只能输入英文字符和数字： ^[A-Za-z0-9]$
  验证qq号码： [0-9]{5,12}
\A: 只匹配字符串开头， \Aabcd, 则abcd

\Z: 仅匹配字符串末尾， abcd\Z, abcd

|: 左右任意一个

(?P...): 分组，除了原来的编号再制定一个别名， (?P12345){2}， 1234512345

(?P=name): 引用分组，
'''
import re
p = re.compile(r'\d+')#编译正则表达式模式，返回一个对象的模式，查找至少包括一个的数字
print(p.findall('ddasw31o31oj4i3j1oj12o3'))#findall是返回字符串中所有不重叠匹配的列表。返回一个列表
print(p.match('eqwewrf2312321dsad',7,14))#表示从字符串哪儿开始找，在哪儿结束
print(re.match('www','www.sina.com'))#尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
print(re.match('www','www.sina.com').group())
print(re.match('www','www.sina.com').span())
print(re.match('com','www.sina.com'))
print(','.join('123456'))#将指定字符添加到字符串中
print('1,2,3,4,5,6'.split(','))#用字符将字符串里的内容分裂开，返回一个列表
'''
re.S(DOTALL)
使.匹配包括换行在内的所有字符
re.I（IGNORECASE）
使匹配对大小写不敏感
re.L（LOCALE）
做本地化识别（locale-aware)匹配，法语等
re.M(MULTILINE)
多行匹配，影响^和$
re.X(VERBOSE)
该标志通过给予更灵活的格式以便将正则表达式写得更易于理解
re.U
根据Unicode字符集解析字符，这个标志影响\w,\W,\b,\B
'''
p1 = re.compile(r'([a-z]+) ([a-z]+)',re.I)
m = p1.match('I LOVe SongYue',2,20)
print(m)
print(m.group(0))#group(0)表示查看所有的组
print(m.start(0))#0的含义是一样的，函数表示从哪里开始
print(m.end(0))#从哪里结束
print(m.group(1))#表示查看第一个组的内容
print(m.start(1))
print(m.end(1))
print(m.groups())#查看所有组
print(m.group())

p2 = re.compile(r'\d+')
print(p2.search('ewew123dsaddf34sd123').span())
print(p2.search('ewew123dsaddf34sd123').group())

p3 = re.compile(r'SunBin')
s = 'I love SunBin'
print(p3.sub(r'SongYue',s))#sub()函数表示替换
#匹配中文
#大部分中文内容表示范围是[u4e00-u9fa5],不包括全角标点
p3 = re.compile(r'[\u4e00-\u9fa5]+')
text = 'hello,world. 你好 世界'
print(p3.findall(text))
