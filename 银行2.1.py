import random
from DBUtils import update
from DBUtils import select
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

    sql= "select count(*) from 开户"
    date = select(sql,[])
    if date[0][0]>=100:
        return 3
    sql1 = "select * from 开户 where account = %s"
    date1 = select(sql1,account)
    if len(date1)!=0:
        return 2
    sql2 = "insert into 开户 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [account,username,password,country,province,street,door,0,bank_name]
    update(sql2,param2)
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
        import pymysql
        con = pymysql.connect(host='localhost',user='root',password='',database='bank')
        curser =con.cursor()
        sql = "select * from 开户 where account = %s"
        curser.execute(sql,account)
        date = curser.fetchone()
        print(date)
        curser.close()
        con.close()
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
        # print(info % (account,name,password,country,province,street,door,users[account]["money"],bank_name))

    elif status == 2:
        print("对不起，该用户已存在！请稍后重试！！！")
    elif status == 3:
        print("对不起，该银行库已满，请携带证件到其他银行办理！！！")
# 存钱
def bank_moneyin(account,money):
    sql = "select * from 开户 where account =%s"
    date = select(sql,account)
    if len(date)!=0:
        sql1 = "update 开户 set money =money + %s where account = %s"
        update(sql1,[money,account])
        return True
    else:
        return False

def moneyin():
    account = input("请输入用户账号：")
    money = input("请输入您的存钱金额：")
    if money.isdigit():
# 将数据传到银行
        status1 = bank_moneyin(account,money)
        if status1 ==True:

            print("存款成功")
        elif  status1 == False :
            print("该银行没有此用户，请重新输入")
    else:
        print("您的输入非法")


# 取钱
def bank_moneyout(account,outmoney,password):

    sql = "select * from 开户 where account =%s"
    date = select(sql,account)

    if len(date) != 0:
        sql1 = "select account from 开户 where mima = %s"
        date1 =select(sql1,password)

        if len(date1) != 0:
            sql2 = "select * from 开户 where account =%s and money >= %s"
            date2 = select(sql2,[account,outmoney])

            if len(date2)!=0:
                sql3 = "update 开户 set money = money - %s where account = %s"
                update(sql3,[outmoney,account])

            else:
                return 3
        else:
            return 2
    else:
        return 1
def moneyout():
    account = input("请输入用户账号:")
    outmoney = input("请输入您要取的金额：")
    password = input("请输入您的取款密码：")
# 将数据传到银行
    status2 = bank_moneyout(account,outmoney,password)
    if outmoney.isdigit():
        if status2 == 1:
            print("您输入的账号不存在，请重新输入")
        elif status2 == 2:
            print("您的密码错误，请重新输入")
        elif status2 == 3:
            print("您的余额不足")
        else:
            print("取款成功")

    else:
        print("输入非法")

# 转账
def bank_moneytransfer (account1,account2,password,moneytransfer):
    sql = "select * from 开户 where account = %s"
    date = select(sql,account1)

    if len(date) != 0:
        sql2 = "select * from 开户 where account = %s"
        date1 = select(sql2,account2)

        if len(date1) !=0:
            sql3 = "select * from 开户 where account = %s and mima = %s"
            date2 = select(sql3,[account1,password])

            if len(date2) !=0:
                sql4 = "select * from 开户 where account= %s and money >=%s"
                date3 = select(sql4,[account1,moneytransfer])

                if len(date3)!=0:
                    sql5 = "update 开户 set money = money - %s where account = %s"
                    update(sql5,[moneytransfer,account1])
                    sql6 = "update 开户 set money = money +%s where account = %s"
                    update(sql6,[moneytransfer,account2])
                    return 0
                else:
                    return 3
            else:
                return 2
        else:
            return 1
def moneytransfer():
    account1 = input("请输入要转出的账户：")
    account2 = input("请输入要转入的账户：")
    password = input("请输入转出账户的密码：")
    moneytransfer = input("请输入要转账的金额：")
    if moneytransfer.isdigit():
# 将数据录入银行
        status3 = bank_moneytransfer(account1,account2,password,moneytransfer)
        if status3 == 0:
            print("成功转出：",moneytransfer,"元")
        elif status3 == 1:
            print("账号错误，请重新输入")
        elif status3 ==2:
            print("转出的账号密码错误")
        elif status3 == 3:
            print("转出的金额不足，请重新输入")
    else:
        print("输入非法")
# 查询
def bank_query(account,password):
    sql = "select * from 开户 where account = %s"
    date = select(sql,account)
    if date!=0:
        sql2 = "select account from 开户 where mima = %s"
        date1 = select(sql2,password)
        if date1!=0:
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
    if status4 == 1:
        sql3 = "select * from 开户 where account = %s"
        date = select(sql3,account)
        if date !=0:
            print("您的信息如下")
            print("当前帐号：", date[0][0], "您的名称：",date[0][1],"密码：", date[0][2], "余额：", date[0][7], "居住地址：",
                "国家：", date[0][3],"省份",date[0][4], "街道：",date[0][5],"门牌号:",date[0][6], "当前的开户行:",date[0][8])
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