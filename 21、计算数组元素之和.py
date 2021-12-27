

# 使用内置函数

arr = [12 , 3 , 4 ,15]
print(sum(arr))

#自定义
def sum_list(arr:list ,n:int )->int:
    sum = 0
    for i in range(n):
        sum += arr[i]
    return sum
arr = [12 , 3 , 4 ,15]
print(sum_list(arr , len(arr)))

#参考方法
from functools import reduce
list = [1 , 3 ,5,4,2,3,3,2]
print(reduce(lambda x,y:x+y , list))

