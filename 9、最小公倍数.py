def CommonMultiple(x , y):
    if x > y:
        x , y = y , x           #保证y永远是最大的
    if y % x == 0:              #当大的数为最大值时，返回最大的数即为公倍数
        return y
    mul = 2                 #倍数至少为2
    while 1 :
        if (y * mul) % x == 0:
            return y*mul
        mul += 1

num1 = int(input("输入一个整数"))
num2 = int(input("输入第二个整数"))
print(num1,"和",num2,"的最小公倍数为:",CommonMultiple(num1, num2))



