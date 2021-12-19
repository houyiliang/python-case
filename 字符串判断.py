str = 'hou yi liang5423297'
print(str.isalnum())                    #判断是否只有数字和字母
print(str.title())              #把每个单词的第一个字母转化成大写其余不变


str1 = "hyl"
print(str1.isalpha())               #判断全为字母
print(str.capitalize())                 #把第一个字母转化成大写字母，其余小写

str2 = "542332974"
print(str2.isdigit())               #判断是否全为数字

str3 = 'houyilioaing4'
print(str3.islower())           #判断是否全为小写
print(str3.upper())                 #把小写都转换成大写

str4 = 'HYLS5'
print(str4.isupper())           #判断所有字符都是大写
print(str4.lower())             #把大写都转化成小写

str = "    "
print(str.istitle())                #判断所有单词首字母是 大写
print(str.isspace())            #判断所有字符都是空白符  \t \n  \r