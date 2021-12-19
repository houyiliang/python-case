
#写文件
with open("test.txt" , "wt") as out_file:
    out_file.write("该文本会自动写入到文件 \n\r 第二行")            #用\n \r表示换行

#读文件
with open("test.txt" , "rt") as in_file:
    text = in_file.read()                                    #读文件时会自动把  \r \n 转换成 \n
print(text)

#文件路径前需要加r取消 \ 转义       或者将‘ \ '  用  ’ \\ ’转义
with open(r'C:\Users\houyiliang\Desktop\test.txt' , 'wt' , encoding="utf-8") as fileout:            #指定格式为utf-8
    fileout.write("第一行测试内容\n")

with open(r'C:\Users\houyiliang\Desktop\test.txt' , 'rt' , encoding='utf-8') as filein:
    text = filein.read()
print(filein.name)
print(text)