'''
Tkinter 常用组件
按钮
  Button                按钮组件
  RadioButton            单选框组件
  CheckButton            选择按钮组件
  Listbox                列表框组件
文本输入组件
  Entry                单行文本框组件
  Text                多行文本框组件
标签组件
  Label                标签组件，可以显示图片和文字
  Message                标签组件，可以根据内容将文字换行
菜单
  Menu                菜单组件
  MenuButton            菜单按钮组件，可以使用Menu代替
滚动条
  scale                滑块组件
  Scrollbar            滚动条组件
其他组件
 Canvas                画布组件
 Frame                框架组件，将多个组件编组
 Toplevel            创建子窗口容器组件
'''
'''
button的属性：

anchor 				设置按钮中文字的对其方式，相对于按钮的中心位置
background(bg) 		设置按钮的背景颜色
foreground(fg)		设置按钮的前景色（文字的颜色）
borderwidth(bd)		设置按钮边框宽度
cursor				设置鼠标在按钮上的样式
command				设定按钮点击时触发的函数
bitmap				设置按钮上显示的位图
font				设置按钮上文本的字体
width				设置按钮的宽度  (字符个数)
height				设置按钮的高度  (字符个数)
state				设置按钮的状态
text				设置按钮上的文字
image				设置按钮上的图片
'''
'''
组件布局
控制组件的摆放方式
三种布局：
pack: 按照方位布局
place: 按照坐标布局
grid： 网格布局

pack布局
最简单，代码量最少，挨个摆放，默认从上倒下，系统自动设置
通用使用方式为： 组件对象.pack(设置，，，，，，，）
side: 停靠方位， 可选值为LEFT,TOP,RIGHT,BOTTON
fill: 填充方式,X,Y,BOTH,NONE
expande: YES/NO
anchor: N,E,S,W,CENTER
ipadx: x方向的内边距
ipady: y
padx: x方向外边界
pady： y........

grid布局
通用使用方式：组件对象.grid(设置,,,,,,,)
利用row，column编号，都是从0开始
stick： N,E,S,W表示上下左右，用来决定组件从哪个方向开始
支持ipadx，padx等参数，跟pack函数含义一样
支持rowspan，columnspan，表示跨行，跨列数量

place布局
明确方位的摆放
相对位置布局，随意改变窗口大小会导致混乱
使用place函数，分为绝对布局和相对布局，绝对布局使用x，y参数
相对布局使用relx，rely, relheight, relwidth
'''
#输入框案例
import tkinter
base = tkinter.Tk()
def login():
    e_1 = e1.get()
    e_2 = e2.get()
    num1 = len(e_1)
    num2 = len(e_2)
    if e_1 == '1007363182' and e_2 == 'sunbin?.':
        b3['text'] = '登陆成功'
    else:
        b3['text'] = '登陆失败'
        e1.delete(0,num1)
        e2.delete(0,num2)
b1 = tkinter.Label(base,text='用户名')
b1.grid(row=0,column=0,stick=tkinter.W)
e1 = tkinter.Entry(base)
e1.grid(row=0,column=1,stick=tkinter.E)

b2 = tkinter.Label(base,text='密码')
b2.grid(row=1,column=0,stick=tkinter.W)
e2 = tkinter.Entry(base)
e2['show'] = '*'
e2.grid(row=1,column=1,stick=tkinter.E)

b3 = tkinter.Label(base,text='')
b3.grid(row=3)

b4 = tkinter.Button(base,text='登陆',command=login)
b4.grid(row=2,column=1,stick=tkinter.E)
base.mainloop()