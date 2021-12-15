#直接调用内置函数
# dec = int(input('输入十进制数字'))
#
# print('十进制数：',dec)
# print('转换为2进制',bin(dec))
# print("转换为八进制",oct(dec))
# print("转换为十六进制",hex(dec))

#自定义
def binary(num):
    l = []
    if num < 0:
        return "-" + binary(abs(num))
    while 1:
        num , reminder = divmod(num , 2)
        l.append(str(reminder))
        if num == 0:
            return " ".join(l[::-1])

print(binary(5))

