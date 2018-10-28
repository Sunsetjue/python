import tkinter
base = tkinter.Tk()
base.title('计算器')
base.geometry('250x380')#定义面板大小
frame1 = tkinter.Frame(width=300,height=150,bg='#dddddd')
frame1.pack()

#定义顶部区域
sv = tkinter.StringVar()
sv.set('0')

label = tkinter.Label(frame1, textvariable=sv, bg='green', width=12, height=1, font=('黑体',20,'bold'), justify='left', anchor='e')
label.pack(padx=10, pady=10)

#定义按键区域
frame2 = tkinter.Frame(width=400, height=350, bg='#cccccc')
frame2.pack(padx=10,pady=10)

def delete():
    number = len(sv.get())
    if number > 1:
        str_number = sv.get()
        list_number = list(str_number)
        list_number = list_number[0:number-1]
        sv.set(str(list_number))
    else:
        sv.set('0')
b_del = tkinter.Button(frame2, text='←', width=5, height=2, command=delete).grid(row=0,column=1)

def clear():
    global num1,num2,operator
    num1 = ''
    num2 = ''
    operator = ''
    sv.set('0')
b_clear = tkinter.Button(frame2, text='AC', width=5, height=2, command=clear).grid(row=0,column=0)

def percent_sign():
    number2 = sv.get()
    number2 = int(number2)/100
    sv.set(str(number2))
b_percent = tkinter.Button(frame2, text='%', width=5, height=2, command=lambda :change('%')).grid(row=0,column=2)

num1 = ''
num2 = ''
operator = ''
def change(num):
    global num1,num2,operator
    if operator == '':
        if num == '%':
            num1 = int(num1)/100
        else:
            num1 = num1 + num
        sv.set(str(num1))
    else:
        if num == '%':
            num2 = int(num2)/100
        else:
            num2 = num2 + num
        sv.set(str(num1)+operator+str(num2))
def operation(op):
    global operator,num1,num2
    if op in ['＋','﹣','×','÷']:
        operator = op
        sv.set(str(num1) + operator)
    else:#如果为等号
        try:
            rst = 0
            if operator == '＋':
                rst = int(num1)+int(num2)
            if operator == '﹣':
                rst = int(num1)-int(num2)
            if operator == '×':
                rst = int(num1)*int(num2)
            if operator == '÷':
                rst = int(num1)/int(num2)
            sv.set(str(rst))
        except Exception as e:
            sv.set('去你妈的报错')
            print(e)
b_chu = tkinter.Button(frame2,text='÷',width=5,height=2,command=lambda :operation('÷')).grid(row=0,column=3)

b7 = tkinter.Button(frame2,text='7',width=5,height=2,command=lambda :change('7')).grid(row=1,column=0)
b8 = tkinter.Button(frame2,text='8',width=5,height=2,command=lambda :change('8')).grid(row=1,column=1)
b9 = tkinter.Button(frame2,text='9',width=5,height=2,command=lambda :change('9')).grid(row=1,column=2)
b_cheng = tkinter.Button(frame2,text='×',width=5,height=2,command=lambda :operation('×')).grid(row=1,column=3)

b4 = tkinter.Button(frame2,text='4',width=5,height=2,command=lambda :change('4')).grid(row=2,column=0)
b5 = tkinter.Button(frame2,text='5',width=5,height=2,command=lambda :change('5')).grid(row=2,column=1)
b6 = tkinter.Button(frame2,text='6',width=5,height=2,command=lambda :change('6')).grid(row=2,column=2)
b_jian = tkinter.Button(frame2,text='－',width=5,height=2,command=lambda :operation('﹣')).grid(row=2,column=3)

b1 = tkinter.Button(frame2,text='1',width=5,height=2, command=lambda :change('1')).grid(row=3,column=0)
b2 = tkinter.Button(frame2,text='2',width=5,height=2,command=lambda :change('2')).grid(row=3,column=1)
b3 = tkinter.Button(frame2,text='3',width=5,height=2,command=lambda :change('3')).grid(row=3,column=2)
b_jia = tkinter.Button(frame2,text='＋',width=5,height=2,command=lambda :operation('＋')).grid(row=3,column=3)

b0 = tkinter.Button(frame2, text='0',width=5,height=2,command=lambda :change('0')).grid(row=4,column=0)
b_deng = tkinter.Button(frame2, text='=',width=5,height=2,command=lambda :operation('=')).grid(row=4,column=1)

base.mainloop()
