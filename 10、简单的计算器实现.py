def divide(x, y):
    if y == 0:
        print("0不能做除数")
        return
    else:
        return x/y

choice = int(input("\n1、相加\n2、相减\n3、相乘\n4、相除\n请输入{1，2，3，4}"))
num1 = int(input("输入第一个数"))
num2 = int(input("输入第二个数"))

if choice == 1:
    print( "{}+{} = {}".format(num1 , num2,num1+num2))
elif choice == 2:
    print("{}-{} = {}".format(num1, num2, num1 - num2))
elif choice == 3:
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif choice == 4:
    print("{} / {} = {}".format(num1, num2, divide(num1 , num2)))



