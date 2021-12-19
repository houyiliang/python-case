import math

lower = int(input("输入区间的下限"))
upper = int(input("输入区间的上限"))
print('素数的结果如下：')
print("="*10)
pri_num = 0         #质数
com_num = 0         #合数
for num in range(lower,upper+1):

    square_num = math.floor(num**0.5)
    if num > 1 :
        for i in range(2,(square_num+1)):
            if(num % i) == 0:
                com_num += 1
                break
            else:
                pri_num += 1
                print(num)
print('='*10)
print(com_num,"个合数")
print(pri_num,"个质数")
