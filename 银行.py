import random
# 1. 空的银行的库 ： 100个
users = {}

# 2.银行的名称写死
bank_name = "中国工商银行的昌平支行"

# 打印欢迎页面
def welcome():
    print("---------------------------------")
    print("-     中国工商银行账户管理系统V1.0     -")
    print("---------------------------------")
    print("-   1.开户                       -")
    print("-   2.存钱                       -")
    print("-   3.取钱                       -")
    print("-   4.转账                       -")
    print("-   5.查询                       -")
    print("-   6.Bye!                       -")
    print("----------------------------------")

# 银行的开户逻辑
def bank_addUser(account,username,password,country,province,street,door):
    # 判断是否已满
    if len(users) >= 100:
        return 3

    # 判断是否存在
    if account in users:
        return 2

    #正常开户
    users[account] = {
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":0,
        "bank_name":bank_name
    }
    return 1


# 用户开户方法
def addUser():
    # 随机获取账号
    li = ["1","2","3","4","5","6","7","8","9","0","a","b","c","e","f"]
    account = ""
    for i in range(8):
        index = random.randint(0, len(li) - 1)
        account = account + li[index]
    name = input("请输入用户名：")
    password = int(input("请输入您的密码（6位数字）："))
    print("接下来要输入您的地址信息：")
    country = input("\t输入国家：")
    province = input("\t输入省份：")
    street =  input("\t输入街道：")
    door = input("\t输入门牌号：")
    # 余额不允许第一次输入，需要存钱

    status = bank_addUser(account,name,password,country,province,street,door)
    if status == 1:
        print("恭喜开户成功！")
        info = '''
            ------------个人信息----------------
            账号：%s,
            用户名：%s,
            取款密码：%s,
            地址信息：
                国家：%s,
                省份：%s,
                街道：%s,
                门牌号：%s,
            余额：%s,
            开户行：%s
            -----------------------------------
        '''
        print(info % (account,name,password,country,province,street,door,users[account]["money"],bank_name))

    elif status == 2:
        print("对不起，该用户已存在！请稍后重试！！！")
    elif status == 3:
        print("对不起，该银行库已满，请携带证件到其他银行办理！！！")
# 存钱
def bank_moneyin(account,savemoney):
    if account in users:
        users[account]["money"] = users[account]["money"]+int(savemoney)
        return True
    else:
        return  False
def moneyin():
    account = input("请输入用户账号：")
    savemoney = input("请输入您的存钱金额：")
    print(users)
# 将数据传到银行
    status1 = bank_moneyin(account,savemoney)
    if status1 ==True:
        print("您的用户名为：",users[account]["username"],"您的账号为：",account)
        print("您的存款金额为：",savemoney,"您的余额为：",users[account]["money"])
    elif  status1 == False :
        print("该银行没有此用户，请重新输入")



# 取钱
def bank_moneyout(account,password,outmoney):
    if account in users:
        if int(password) == users[account]["password"]:
            if int(outmoney) <= users[account]["money"]:
                users[account]["money"]=users[account]["money"]-int(outmoney)
            else:
                return 3
        else:
            return 2
    else:
        return  1
def moneyout():
    account = input("请输入用户账号:")
    outmoney = int(input("请输入您要取的金额："))
    password = int(input("请输入您的取款密码："))
# 将数据传到银行
    status2 = bank_moneyout(account,outmoney,password)
    if int(outmoney) >0:
        if status2 == 1:
            print("您输入的账号不存在，请重新输入")
        elif status2 == 2:
            print("您的密码错误，请重新输入")
        elif status2 == 3:
            print("您的余额不足")
        else:
            print("恭喜您，取款成功！您的余额为：",users[account]["money"])
    else:
        print("请输入正确的金额")


# 转账
def bank_moneytransfer (account1,account2,password,moneytransfer):
    if account1 in users:
        if account2 in users:
            if password == users[account1]["password"]:
                if int(moneytransfer) >0:
                    if int(moneytransfer) <= users[account1]["money"]:
                        return 0
                    else:
                        return  3
                else:
                    print("输入非法字符，请重新输入")
            else:
                return 2
        else:
            return 1
    else:
        return 1
def moneytransfer():
    account1 = input("请输入要转出的账户：")
    account2 = input("请输入要转入的账户：")
    password = int(input("请输入转出账户的密码："))
    moneytransfer = int(input("请输入要转账的金额："))
# 将数据录入银行
    status3 = bank_moneytransfer(account1,account2,password,moneytransfer)
    if status3 == 0:
        print("成功转出：",moneytransfer,"元")
        print("转出账户",account1,"余额为：",users[account1]["money"]-moneytransfer)
        print("转入账户",account2,"余额为：",users[account2]["money"]+moneytransfer)
    elif status3 == 1:
        print("账号错误，请重新输入")
    elif status3 ==2:
        print("转出的账号密码错误")
    elif status3 == 3:
        print("转出的金额不足，请重新输入")

# 查询
def bank_query(account,password):
    if account in users:
        if password == users[account]["password"]:
            return 1
        else:
            return 2
    else:
        return 3
# 数据录入到银行
def query():
    account = input("请输入要查询的账户号：")
    password = int(input("请输入账户密码："))
    status4 = bank_query(account,password)
    if status4 == True:
        print("您的信息如下")
        print("当前帐号：", account, "密码：", password, "余额：", users[account]['money'], "居住地址：", users[account]
        ["country"], users[account]["province"], users[account]["street"], users[account]["door"], "当前的开户行",
              bank_name)
    elif status4 == 2:
        print("密码输入错误，请重新输入")
    elif status4 == 3:
        print("用户不存在，请重新输入")

while True:
    welcome()
    num = input("请输入业务编号：")
    if num.isdigit():
        num = int(num)
        if num == 1:
            addUser()
        elif num == 2:
            moneyin()
        elif num ==3:
            moneyout()
        elif num ==4:
            moneytransfer()
        elif num == 5:
            query()
        elif num == 6:
            print("欢迎下次光临")
            break
        else:
            print("您输入非法，请重新输入")