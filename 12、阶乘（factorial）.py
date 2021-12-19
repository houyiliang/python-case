##自己写的
# num = int (input("输入一个数"))
# factorial = 1
#
# while 1:
#     if num < 0:
#         num = int (input("输入一大于0的数"))
#     elif num == 0:
#         print("0的阶乘为1")
#         break
#     else:
#         for i in range(1 , num + 1):            #range相当于右开区间
#             factorial = factorial * i
#         print("%d的阶乘为%d"%(num,factorial))
#         break




# #自带函数
# import math
# num = int(input("请输入一个数字："))
# print("{0}的阶乘为{1}".format(num,math.factorial(num)))



##运用的递归递归                           但递归的层数不能超过1000
# def factorial(n):
#     if n > 1:
#         return n*factorial(n-1)
#     return 1
# while 1 :
#     try:
#         n = input("请输入一个数字（输入q退出）")
#         if n =="q":
#             break
#         n = int(n)
#         if n < 1:
#             raise ValueError
#         x = factorial(n)
#         print(x)
#     except ValueError:
#         print("请重新输入数字")
