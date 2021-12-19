
Upperlimit = int(input("输入上限整数"))
Lowerlimit = int(input("输入下限整数"))

for num in range(Lowerlimit,Upperlimit+1):

    numlen = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digits = temp % 10
        sum += digits**numlen
        temp //= 10
    if num == sum:
        print(num,end=",")




