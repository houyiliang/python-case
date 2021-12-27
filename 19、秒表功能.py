import tkinter
import time

star = time.time()


def gettime():
    elap = time.time() - star  # 获取时间差
    minutes = int(elap / 60)
    seconds = int(elap - minutes * 60.0)
    hseconds = int((elap - minutes * 60.0 - seconds) * 1000)
    var.set('%02d:%02d:%03d' % (minutes, seconds, hseconds))
    root.after(1, gettime)  # 每隔1ms调用函数自身获取时间


root = tkinter.Tk()         #创建一个窗口
root.title('电子时钟')
var = tkinter.StringVar()       #在使用界面编程的时候，有些时候是需要跟踪变量的值的变化，以保证值的变更随时可以显示在界面上
lb = tkinter.Label(root, textvariable=var, fg='red', font=("微软雅黑", 100))  # 设置字体大小颜色
'''
如果你知道连环画，你可以理解为，每个部件都是连环画。root到root.pack()就是你设计连环画。mainloop就是去翻它
'''
lb.pack()           #root.pack() 就是设计你的部件的类型，尺寸，样式，位置，   相当于提前存放多张图
gettime()
root.mainloop()     #mainloop就进入到事件（消息）循环。一旦检测到事件，就刷新组件。        其实就是刷新

#   参考链接    https://blog.csdn.net/wangfei8348/article/details/51744968
