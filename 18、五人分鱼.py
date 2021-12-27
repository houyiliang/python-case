'''

A、B、C、D、E 五人在某天夜里合伙去捕鱼，到第二天凌晨时都疲惫不堪，于是各自找地方睡觉。

日上三杆，A 第一个醒来，他将鱼分为五份，把多余的一条鱼扔掉，拿走自己的一份。

B 第二个醒来，也将鱼分为五份，把多余的一条鱼扔掉拿走自己的一份。 。

C、D、E依次醒来，也按同样的方法拿鱼。

问他们至少捕了多少条鱼?
'''

def fish1():

    fish = 1
    while 1:
        total = fish
        flag = 1                #作为记号
        for i in range(5):              #循环5次
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4            #一共5份   除去拿走那一份
            else:
                flag = 0            #总数不满足条件跳出循环，  鱼的数量+1
                break
        if flag:            #满足条件
            print(f'总共有{fish}条鱼')
            break
        fish += 1

#递归





if __name__ =='__main__':
    fish1()