# a = ("呵呵","aa","aa","qq","ee","tt","hh")
# print(a[3])
# print(a.index("hh")) # 位数
# print(a.count("aa")) # 统计个数
# print(a[3:4]) # 切片
# print(a[:4]) # 切片 左开右闭 0到4
# print(a[3:]) # 切片 左开右闭 3到最后
# b = (a,"mm","nn","bb")
# print(b[0][4]) #二维元组

# c = [1,4,5,6,7,"q","ww"]
# c.append("haha") #在元组末尾添加数据
# c.insert(2,"jaj")
# print(c)
# b = c.pop(0) #剪切 将数组的数据拿出来用
# d = c.pop(0) 
# print(c)
# print(b)
# print(d)
# xx = ["nihao","buaho"]
# print(c+xx)
# print(c)
# a = c[3]
# print(a)
"""
所有的方法都是小括号结尾 print  input insert len
元组,数组,字典的[取值]都用中括号
 ()   {}   {}
"""
"""
字典的特点
1.字典中的值没有顺序
2.字典的接口必须是键值对 key:value
"""
a = {"name":"cc"}
#取值
print(a["name"])
#新增
a["high"] = "189cm"
print(a)
#修改
a["name"] = "gihub"
print(a)

b = a.get("name")
print(b)
c = a.pop("name")
print(c)
a.update(name=1111)
print(a)
#数组和字典的删除'
del a["name"]
a.update(nam = "aaa")
print(a)