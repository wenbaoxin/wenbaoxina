name = "root"
password = "admin"
count = 0
count = count +1
while count<4:
    count = count + 1
    name1 =input("请输入用户名：")
    password1 = input("请输入密码：")
    if name1 == name and password1 == password:
        print("登录成功")
    elif password1 != password:
        print("密码错误")
print("密码锁定")
