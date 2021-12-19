#引入日历模块
import calendar

calendar.setfirstweekday(firstweekday=6)    #设置第一天是星期天
while 1:
    year = int(input("请输入年份："))
    #month1 = int(input("输入月份"))
    for i in range(12):
        print(calendar.month(year, i+1))
        print("*"*20)





