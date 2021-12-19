#定义
li = ['a' , 'b' , 'houyiliang' , 'liujie' , 'xiexie']
#索引
print(li[-1])
print(li[1:-1])             #不包括最后一个


#增加
li.append('love')
li.insert(2 , 'I')          #插到索引为2的位置

li.extend(["you","forgive"])
li = li + ['还请原谅我']
li = li + ['love' , 'you'] * 3



#搜索
print(li.index('liujie') , li.index('houyiliang'))

#删除
li.remove('a')          #删除首次出现的一个值         第二个不删除    若没有找到会引发异常
li.pop(0)                   #通过索引删除
li.pop()                #删除最后一个元素

#拼接 和 拆分
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
li=[]
li=["%s=%s" % (k, v) for k, v in params.items()]            #params  索引和值一起遍历
print(li)
s = ";".join(li)        #把list链接成字符串   s是字符串， li是列表
print(s , type(s))
li2 = s.split(";")           #把字符串切分成列表
print(li2 , type(li2))

#映射
li = [5 , 4 , 2 , 3]
li = [elem * 2 for elem in li]
print(li)

#字典的解析
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print(params.keys())
print(params.values())
print(params.items())               #items() 方法的遍历：items() 方法把字典中每对 key 和 value 组成一个元组，并把这些元组放在列表中返回
for k , v in params.items():
    print(k)
    print(v)
    print("{} = {}".format(k ,v))
    print("%s = %s" %(k ,v))



#list过滤
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
li2 = [elem for elem in li if len(elem) > 1]

li3 = [elem for elem in li if elem != "b"]

li4 = [elem for elem in li if li.count(elem) == 1]
