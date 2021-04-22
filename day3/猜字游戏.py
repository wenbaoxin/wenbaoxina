import random
num = random .randint(1,100)
count = 0
gold = 0
while count<7 :
    count = count + 1
    gold = gold+2500
    num1 = input("请输入你想猜的数：")
    num1 = int(num1)
    if num1 != num and num1 < num:
        print("小了，""您现在猜了：",count,"次","花费金币：",gold,"枚")
    elif num1 > num :
        print("大了，""您现在猜了：",count,"次","花费金币：",gold,"枚")
    else:
        print("恭喜您，猜中了中奖数字！！！数字为：",num,"您猜的次数为：",count,"次","此次花费金币：",gold,"枚")
    if count == 7:
            print("您的次数用尽了，共花费：",gold,"枚金币","正确答案是：",num)