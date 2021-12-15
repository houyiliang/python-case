# nterms = int(input("你需要几项"))
#
# n1 = 0
# n2 = 1
# count = 2
#
# if nterms <= 0:
#     print("输入一个正数")
# elif nterms == 1:
#     print("斐波那契额数列",n1)
# else:
#     print("斐波那契数列：")
#     print(n1,",",n2,end=",")
#     while(count < nterms):
#         nth = n1 + n2
#         print(nth , end =",")
#         n1 = n2
#         n2 = nth
#         count += 1



# #递归实现
# def fibo(n):
#     a = 0
#     b = 1
#     while a < n:
#         print(a,end=" ")
#         a , b = b , a + b
# fibo(1000)