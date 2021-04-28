coupon = []
coupon1 = ["1张辣条优惠券满300减299"]
coupon2 = ["1张活鬼优惠券满2000减1000"]
coupon.append(coupon1)
coupon.append(coupon2)
import random
a = coupon[random.randint(0,len(coupon)-1)]
b = []
c = []
d = []
print("死鬼，恭喜你获得：",a,"快去购物吧")
shop = [
    ["带定义的秋裤",99.9],
    ["护膝",49.9],
    ["卫龙面筋",333.5],
    ["三只松鼠大礼盒",779.9],
    ["可口可乐/提",399],
    ["炫龙dd2",5999],
    ["卡西欧",1299],
    ["小熊饼干",489],
    ["现抓的活鬼",2999]
]
salary = int(input("请输入您的薪资："))
salary = int(salary)
salary1 = salary
salary = int(salary1)
mycart = []
while True:
    for index , value in enumerate(shop) :
        print( index , "    ",value)
    num = input("请输入商品编号：")
    if num .isdigit():
        num = int(num)
        if num >=len(shop):
            print("死鬼，我们有这个商品编号吗？啊？")
        else:
            if salary >=int(shop[num][1]):
                mycart.append(shop[num])
                d.append(shop[num][1])
                print(d)
                print("您的购物车有：",mycart)
            else:
                print("穷鬼，钱不够了来什么商城，拜拜了您嘞")
    elif num =="q" or num=="Q":
        print("------------欢迎下次光临！死鬼--------------")
        break
    else:
        print("输入非法，请重新输入")
for i in mycart:
    if i == shop[2]:
        b.append(shop[2])
        if a == coupon1:
            use = input("是否使用辣条优惠券：")
            if use == "是":
                if b[0][1] >= 300:
                    salary= salary - sum(d) + 299
                else:
                    salary= salary - sum(d)
                print("打折完消费为：", salary)
            elif use == "否":
                salary= salary - sum(d)
        else:
            salary= salary - sum(d)
    elif i == shop[8]:
        c.append(shop[8])
        if a == coupon2:
            use = input("是否使用活鬼优惠券：")
            if use == "是":
                if c[0][1] >= 2999:
                    salary= salary - sum(d) + 1000
                else:
                    salary= salary - sum(d)
                print("打折完消费为：", salary)
            elif use == "否":
                salary = salary - sum(d)
        else:
            salary = salary - sum(d)
    else:
        print("本次无优惠券可用")
        salary= salary - sum(d)
print("您本次购物如下：")
for index,value in mycart:
    print(index, " ", value)
if salary<=salary1:
    integral = (salary1-salary)//10
    print("您的余额为：",salary,"您的积分为：",integral)
else:
    print("您的余额不足")







