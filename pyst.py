print("--这是一个小游戏叫做你们俩说字数我算你们说了多少字--")
b = input("请嗦：")
c = input("请嗦：")
a = b + c
print("字数相加长度是",len(c+b))
if a == b + c:
    print("我可真厉害")