
'''
项目分析
屏保可以自己启动，也可以手动启动
一旦敲击键盘或者移动鼠标后，或者其他的引发时间，则停止
如果屏保是一幅画的话，则没有画框
图像的动作是随机的，具有随机性，可能包括颜色，大小，多少， 运动方向，变形等
整个世界的构成是：

ScreenSaver:

需要一个canvas， 大小与屏幕一致，没有边框
Ball

颜色，大小，多少， 运动方向，变形等随机
球能动，可以被调用
'''
import random
import tkinter
class Ball():
    # 定义球运动的类
    def __init__(self,canvas,scrnwidth,scrnheight):
        # canvas: 画布，所有的内容应该在屏幕上呈现出来，此处通过变量传入
        # scrn_width表示屏幕的宽， scrn_height表示屏幕高
        #定义球圆心出现的初始位置
        self.xcoordinate = random.randint(5,int(scrnwidth-5))#定义球出现的X轴的圆心位置
        self.ycoordinate = random.randint(2,int(scrnheight)-3)#定义球出现的Y轴的圆心的位置
        #定义球运动的速度
        self.xspeed = random.randint(4,20)
        self.yspeed = random.randint(3,15)
        #定义球的大小，半径
        self.size = random.randint(10,50)
        #定义屏幕的大小
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight
        self.canvas = canvas
        #定义球的颜色
        # 颜色表示的方法：RGB表示法：三个数字，每个数字都在0～255之间，表示红绿蓝三个颜色之间的大小
        #此处用lambda表达式
        c = lambda :random.randint(0,255)
        self.color = '#%02x%02x%2x' % (c(),c(),c())
        #最后需要在画布上画出一个个球
        # tkinter没有画圆形函数
        # 只有一个画椭圆函数，画椭圆需要定义两个坐标，
        # 在一个长方形内画椭圆，我们只需要定义长方形左上角和右下角就好
        # 求两个坐标的方法是，已知圆心的坐标，则圆心坐标减去半径能求出
        # 左上角坐标，加上半径能求出右下角坐标
    def create_ball(self):
        x1 = self.xcoordinate - self.size
        y1 = self.ycoordinate + self.size
        x2 = self.xcoordinate + self.size
        y2 = self.ycoordinate - self.size
            # 定义好左上角和右下角坐标后，进行画圆，填充圆的内部颜色和画出外圈的圈
        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color,outline=self.color)

            #球创造出来了，则要实现球的移动
    def move_ball(self):
        self.xcoordinate += self.xspeed
        self.ycoordinate += self.yspeed
            #移动会撞墙，撞完墙则要回头
        if self.ycoordinate + self.size >= self.scrnheight:
            self.yspeed *= -1
        elif self.xcoordinate + self.size >= self.scrnwidth:
            self.xspeed *= -1
        elif self.ycoordinate <= self.size:
            self.yspeed *= -1
        elif self.xcoordinate <= self.size:
            self.xspeed *= -1
                #移动球的时候，需要球移动的速度
        self.canvas.move(self.item,self.xspeed,self.yspeed)
class ScreenProtect():
    def __init__(self,num_balls):
        self.balls = []  # 创建一个列表用来装球
        #每次屏保出现的球的数量是随机的
        self.num_balls = random.randint(8,15)
        self.root = tkinter.Tk()
        #取消边框
        self.root.overrideredirect(1)
        #任何鼠标的移动都要取消屏保
        self.root.bind('<Motion>',self.myquit)
        self.root.bind('<Key>',self.myquit)
        #求出屏幕的高和宽
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        #创建画布，包括画布的规格，大小，归属
        self.canvas = tkinter.Canvas(self.root,width=w,height=h)
        self.canvas.pack()
        for i in range(self.num_balls):
            ball = Ball(self.canvas,scrnwidth=w,scrnheight=h)
            ball.create_ball()
            self.balls.append(ball)

        self.run_screen_saver()
        self.root.mainloop()
    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()
        self.canvas.after(200,self.run_screen_saver)# after表达式是系统自带的函数，表示200毫秒后启动后面一个函数
    #定义停止的时候，什么时候屏保该停
    def myquit(self,e):
        self.root.destroy()
#调用程序
if __name__ == '__main__':
    ScreenProtect(15)


