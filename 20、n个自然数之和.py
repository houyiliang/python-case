
def sum_num(n):
    sum = 0
    for i in range(n+1):
        sum += i**3
    return sum

print(sum_num(7))