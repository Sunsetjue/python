'''
构成：

蛇 Snake
食物 Food
世界 World
蛇和食物属于整个世界

  class World:
      self.snake
      self.food
上面代码不太友好
我们用另外一个思路来分析
我们的分析思路

食物是一个独立的事物
蛇也可以认为是一个独立的事物
世界也是，但世界负责显示
'''
import random
import threading
import time
from tkinter import *
import queue
#定义一个食物的类。功能：1 随机出现在世界的某个地方  2 蛇吃后可以增加分数 3 蛇吃后身体会变长
class Food():
    def __init__(self,queue):
        self.queue = queue
        self.new_food()
    def new_food(self):#z在世界上随机产生一个坐标
        x = random.randrange(5, 480, 10)
        y = random.randrange(5, 295, 10)
        self.position = x,y#position表示存放食物的地方
        self.exppos = x - 5, y - 5, x + 5, y + 5
        # 队列，就是一个不能够随意访问内部元素，只能从头弹出一个元素并只能
        # 从队尾追加元素的list
        #  把一个食物产生的消息放入队列
        # 消息的格式，自己定义
        # 我的定义是： 消息是一个dict， k代表消息类型，v代表此类型的数据
        self.queue.put({'food':self.exppos})
class Snake(threading.Thread):
    def __init__(self,world,queue):#定义world和queue是因为在这个类里面是需要用的
        threading.Thread.__init__(self)
        self.direction = 'Left'
        self.world = world
        self.queue = queue
        self.daemon = True
        self.point_earned = 0
        self.food = Food(queue)#定义食物
        self.snake_points = [(495,55),(485,55),(475,55),(465,55),(455,55)]
        self.start()
    def run(self):
        '''
        启动多线程所必须要有的函数
        :return:
        '''
        if self.world.is_game_over:#游戏结束的时候的函数
            self._delete()
        while not self.world.is_game_over:#游戏没有结束时则一直运行
            self.queue.put({'move':self.snake_points})
            time.sleep(0.9)#定义运行速度
            self.move()
    def cal_new_position(self):
        #计算新的蛇头出现的位置
        last_x,last_y = self.snake_points[-1]
        if self.direction == 'Up':#direction负责表示蛇移动的方向
            new_snake_point = last_x,last_y-10#每次移动的像素为10
        elif self.direction == 'Left':
            new_snake_point = last_x-10,last_y
        elif self.direction == 'Right':
            new_snake_point = last_x+10,last_y
        elif self.direction == 'Down':
            new_snake_point = last_x,last_y+10
        return new_snake_point
    def move(self):
        new_snake_point = self.cal_new_position()
        if self.food.position == new_snake_point:#如果蛇吃到食物，计分并且重新定义一个食物
            add_snake_point = self.cal_new_position()
            self.snake_points.append(add_snake_point)
            self.point_earned += 1
            self.queue.put({'point_earned':self.point_earned})
            self.food.new_food()
        else:#如果没有吃到食物，则继续移动，如果撞墙，则游戏结束
            #移动的时候，第一个被移除，最后一个增加
            self.snake_points.pop(0)
            #判断蛇是否会装上墙，即判断程序是否退出
            self.check_game_over(new_snake_point)
            self.snake_points.append(new_snake_point)
    def key_pressd(self,e):
        self.direction = e.keysym
    def check_game_over(self,snake_point):
        x,y = snake_point[0],snake_point[1]
        if not -5 < x < 505 or not -5 < y < 315 or snake_point in self.snake_points:
            self.queue.put({'game_over': True})

class World(Tk):
    def __init__(self,queue):
        Tk.__init__(self)
        self.queue = queue
        self.is_game_over = False
        #定义画板
        self.canvas = Canvas(self,width=495,height=305,bg='#000000')
        self.canvas.pack()
        #把蛇和分数还有食物添加到画板中
        self.snake = self.canvas.create_line((0,0),(0,0),fill='#FFFF00',width=10)
        self.food = self.canvas.create_rectangle(0,0,0,0,fill='#00FF00', outline='#00FF00')
        self.point_earned = self.canvas.create_text(455,15,fill='white',text='score: 0')
        self.queue_handler()
    def restart(self):
        self.destroy()
        main()
    def queue_handler(self):
        try:
            while True:
                task = self.queue.get(block=False)
                if task.get('game_over'):
                    self.game_over()
                elif task.get('move'):#游戏没有结束的时候，继续移动
                    points = [x for point in task['move'] for x in point]
                    # 重新绘制蛇
                    self.canvas.coords(self.snake,*points)
                elif task.get('food'):
                    self.canvas.coords(self.food,*task['food'])
                elif task.get('point_earned'):
                    self.canvas.itemconfigure(self.point_earned,
                                              text='score:{}'.format(task['point_earned']))
                    self.queue.task_done()
        except queue.Empty:
            if not self.is_game_over:
                    # after的含义是，在多少毫秒后调用后面的函数
                self.canvas.after(100, self.queue_handler)
    def game_over(self):
        self.is_game_over = True
        self.canvas.create_text(220, 150, fill='white',text='Game over')
        pb = Button(self,text='Quit',command=self.destroy)
        rb = Button(self,text='Again',command=self.restart)
def main():
    q = queue.Queue()
    world = World(q)

    snake = Snake(world, q)

    world.bind('<Key-Left>', snake.key_pressd)
    world.bind('<Key-Right>',snake.key_pressd)
    world.bind('<Key-Up>',snake.key_pressd)
    world.bind('<Key-Down>',snake.key_pressd)
    # 同样绑定右键，上下键
    world.mainloop()
if __name__ == '__main__':
    main()





