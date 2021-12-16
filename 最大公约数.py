def CommonDivisor(x , y):
    if x > y:
        x , y = y , x               #保证 x 永远最小
    if y % x == 0:                      #当最小值为最大公约数时直接返回
        return x
#当最小值不为最大公约数时，最大公约数不会大于最小值的1/2    遍历最大公约数从大到小遍历能减少遍历次数
    for i in range(x//2+1, 1 ,-1):
        if (x % i == 0) and (y % i == 0):
            return i
    return 0
num1 = int(input("请输入第一个数字"))
num2 = int(input("请输入第二个数字"))
print(num1,"和",num2,"的最大公约数为：" ,CommonDivisor(num1 , num2) )