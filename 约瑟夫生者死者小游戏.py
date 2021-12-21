
'''
30 个人在一条船上，超载，需要 15 人下船。

于是人们排成一队，排队的位置即为他们的编号。

报数，从 1 开始，数到 9 的人下船。

如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？
'''
def yuesefu1():
    people ={}
    for i in range(1 , 31):         #创建30大小的字典  键为1-30  值为 1  代表在船上
        people[i] = 1

    check = 0       #  控制喊的数
    count = 0           #用来统计跳下去的人数
    x = 1              #用来统计编号
    while x <= 31:
        if x == 31:
            x = 1               # 若编号等于31， 则将它赋为1， 让它重新开始
        elif count == 15:       #退出循环的条件
            break
        else:
            if people[x] == 0:      #满足下船条件  游戏继续
                x += 1
                continue
            else:
                check += 1      #报数+1
                if check == 9:
                    people[x] = 0
                    check = 0           #报数继续从0开始
                    print("{}号下水了".format(x))
                    count += 1
                else:
                    x += 1
                    continue

def yuesefu2():
    people = list(range(1,31))
    while len(people) > 15:
        i = 1                  #重新开始
        while i < 9:
            people.append(people.pop(0))        #每次报数的前 8 个人存放在people列表中
            i += 1
        print('{:2d}号下船了'.format(people.pop(0)))        #第9次跳出循环即报数第9个人下船

def yuesefu3(nums , step , stay):           #nums  人数    step  数到几的步数   stay  最后留下多少人
    lists = list(range(1 , nums+1))
    check = 0           #统计报数
    while len(lists) > stay:
        for i in lists[:]:      #遍历所有人
            check += 1
            if check == 9:
                check = 0       #从1开始
                lists.remove(i)     #移掉下船的人
                print("{}号下船了".format(i),end="   ")
    return lists


stay=yuesefu3(30 , 9  , 15)
print("最后留下来的人", stay)




