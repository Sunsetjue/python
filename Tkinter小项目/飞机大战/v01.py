import tkinter
#画出世界.包括背景和蜜蜂
if __name__ == '__main__':
    base = tkinter.Tk()
    base.title('飞机大战')
    base.resizable(width=False,height=False)
    main_canvas = tkinter.Canvas(base,width=480,height=600)
    main_canvas.pack()
    img_name = 'C:\\Users\\l\\PycharmProjects\\sunbin_1\\Tkinter小项目\\飞机大战\\img\\background.gif'
    img_background = tkinter.PhotoImage(file=img_name)
    #利用create_image将图片画在画布上面
    main_canvas.create_image(240,300,anchor=tkinter.CENTER,image=img_background,tags='background')

    img_name = 'C:\\Users\\l\\PycharmProjects\\sunbin_1\\Tkinter小项目\\飞机大战\\img\\bee.gif'
    img_bee = tkinter.PhotoImage(file=img_name)
    #利用create_image将图片画在画布上面
    main_canvas.create_image(240,300,anchor=tkinter.CENTER,image=img_bee,tags='bee')
    base.mainloop()
