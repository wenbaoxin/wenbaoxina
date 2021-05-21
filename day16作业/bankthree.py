import random
from DBUtils import update
from DBUtils import select
# 2.银行的名称写死
bank_name = "中国工商银行的昌平支行"

# 打印欢迎页面
# class Welcome:
#     info="""
#     **********************
#     * 中国工商银行管理系统  *
#     **********************
#     *  1.开户             *
#     *  2.存钱             *
#     *  3.取钱             *
#     *  4.转账             *
#     *  5.查询             *
#     *  6.拜拜             *
#     """
#     def welcome(self):
#         print(self.info)

# 用户类
class User:
    __account=""
    __username=""
    __password=0
    __address=None
    __money=0
    __bank_name=""
    def setAccount(self,account):
        self.__account=account
    def getAccount(self):
        return self.__account

    def setUserame(self,username):
        self.__username=username
    def getUsername(self):
        return self.__username

    def setPassword(self,password):
        self.__password=password
    def getPassword(self):
        return self.__password

    def setMoney(self,money):
        self.__money=money
    def getMoney(self):
        return self.__money




class Address:
    country=""
    provience=""
    street=""
    door=""

    def setCountry(self,country):
        self.__country=country
    def getCountry(self):
        return self.__country

    def setProvience(self,provience):
        self.__provience=provience
    def getProvience(self):
        return self.__provience

    def setStreet(self,street):
        self.__street=street
    def getStreet(self):
        return self.__street


    def setDoor(self,door):
        self.__door=door
    def getDoor(self):
        return self.__door
# 逻辑方法类
# 添加用户
class bank_adduser:
 def addbank_adduser(self,u,a):
     sql = "select count(*) from 开户"
     data = select(sql,[])
     if data[0][0] >= 100:
         return 3

     sql1="select * from 开户 where account=%s"
     data1=select(sql1,u.getAccount())
     if len(data1)!=0:
         return 2
     sql2="insert into 开户 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
     param=[u.getAccount(),u.getUsername(),u.getPassword(),a.getCountry(),a.getProvience(),a.getStreet(),a.getDoor(),u.getMoney(),bank_name]
     update(sql2,param)
     return 1
#  存款逻辑
 def savemoney(self,u):
     sql = "select * from 开户 where account=%s "
     data = select(sql, u.getAccount())
     if len(data) != 0:
         sql1 = "update 开户 set money = money + %s  where account = %s;"
         update(sql1, [u.getMoney(), u.getAccount()])
         return 1
     else:
         return False
# 取款逻辑
 def getmoney(self,u):
     sql = "select * from 开户 where account=%s  "
     date = select(sql, u.getAccount())
     if len(date) != 0:
         sql2 = "select account from 开户 where account=%s and  mima=%s"
         date = select(sql2, [u.getAccount(),u.getPassword()])
         if len(date) != 0:
             sql4 = "select * from 开户 where account = %s and money>=%s"
             date = select(sql4, [u.getAccount(),u.getMoney()])
             if len(date) != 0:
                 sql3 = "update 开户 set money = money - %s  where account = %s"
                 update(sql3, [u.getMoney(), u.getAccount()])
                 return 0
             else:
                 return 3
         else:
             return 2
     else:
         return 1
# 转账逻辑
 def transfer(self,u,inu):
     sql = "select * from 开户 where account=%s  "
     data = select(sql, u.getAccount())
     if len(data) != 0:
         sq2 = "select * from 开户 where account=%s  "
         data1 = select(sq2, inu)
         if len(data1) != 0:
             sql3 = "select account from 开户 where account=%s and mima=%s"
             data = select(sql3, [u.getAccount(), u.getPassword()])
             if len(data) != 0:
                 sql4 = "select * from 开户 where account = %s and money>=%s"
                 data = select(sql4, [u.getAccount(),u.getMoney()])
                 if len(data) != 0:
                     sql5 = "update 开户 set money=money-%s where account = %s "
                     update(sql5, [u.getMoney(), u.getAccount()])
                     sql6 = "update 开户 set money=money+%s where account = %s "
                     update(sql6, [u.getMoney(), inu])
                     return 0
                 else:
                     return 3
             else:
                 return 2
         else:
             return 1
     else:
         return 1
# 查询逻辑
 def inquriy(self,u):
     sql = "select * from 开户 where account=%s  "
     data = select(sql, u.getAccount())
     if len(data) != 0:
         sql2 = "select account from 开户 where mima=%s"
         data = select(sql2, u.getPassword())
         if len(data) != 0:
             return 0
         else:
             return 2
     else:
         return 1



# 输入方法类
# 开户输入
class shuru:
    def kaihu(self):
        u = User()
        u.setAccount(random.randint(10000000,99999999))
        u.setUserame(input("请输入用户姓名："))
        u.setPassword(input("请输入密码："))
        a = Address()
        a.setCountry(input("请输入国家："))
        a.setProvience(input("请输入省份："))
        a.setStreet(input("请输入街道："))
        a.setDoor(input("请输入门牌号："))
        statue=bank_adduser().addbank_adduser(u,a)
        if statue == 1:
            info="""
               ----------个人信息----------
                       账号：%s
                       姓名：%s
                       密码：%s
                       地址：
                           国家：%s
                           省份：%s
                           街道：%s
                           门牌号：%s
                       余额：%s
                       开户行：%s
                       ---------------------------
            """
            print("开户成功！！")
            print(info%(u.getAccount(),u.getUsername(),u.getPassword(),a.getCountry(),a.getProvience(),a.getStreet(),a.getDoor(),u.getMoney(),bank_name()))
        elif statue == 2:
            print("用户已存在！")
        elif statue == 3:
            print("用户已满，去其他银行吧！")
# 存款输入
    def save_money(self):
        u = User()
        u.setAccount(input("请输入账号："))
        u.setMoney(input("请输入存款金额："))
        money1 = bank_adduser().savemoney(u)
        if money1 == 1:
            print("存款成功！")
        else:
            print("用户不存在！")
# 取款输入
    def get_money(self):
        u = User()
        u.setAccount(input("请输入账号："))
        u.setPassword(input("请输入密码："))
        u.setMoney(input("请输入取款金额："))
        money1 = bank_adduser().getmoney(u)
        if money1 == 0:
            print("恭喜你，取款成功!")
        elif money1 == 1:
            print("账号不存在！")
        elif money1 == 2:
            print("密码错误！")
        elif money1 == 3:
            print("你的钱不够！")
# 转账输入
    def transfer_money(self):
        u=User()
        u.setAccount(input("请输入转出账号："))
        inu=(input("请输入转入账号："))
        u.setPassword(input("请输入密码："))
        u.setMoney(input("请输入转出金额："))
        outmoney1=bank_adduser().transfer(u,inu)
        if outmoney1 == 0:
            print("转账成功！成功转出")
        elif outmoney1 == 1:
            print("账户不存在！")
        elif outmoney1 == 2:
            print("密码错误！")
        elif outmoney1 == 3:
            print("你的钱不够！")
# 查询输入
    def bank_inquriy(self):
        u=User()
        u.setAccount(input("请输入账号："))
        u.setPassword(input("请输入密码："))
        account1 = bank_adduser().inquriy(u)
        if account1 == 0:
            sql = "select * from 用户信息 where account=%s  "
            date = select(sql, u.getAccount())
            if len(date) != 0:
                print("账号：", date[0][0],
                      "账户名", date[0][1],
                      "密码：", date[0][2],
                      "居住地址：", date[0][3], date[0][4], date[0][5], date[0][6],
                      "余额：", date[0][7],
                      "当前账户开户行：", date[0][8])
        elif account1 == 1:
            print("账户不存在！")
        elif account1 == 2:
            print("密码错误！")
# while True:
#     # Welcome().welcome()
#     num = input("请输入您的业务编号：")
#     if num.isdigit():
#         num = int(num)
#         if num == 1:
#             shuru().kaihu()
#         elif num == 2:
#             shuru().save_money()
#         elif num == 3:
#             shuru().get_money()
#         elif num == 4:
#             shuru().transfer_money()
#         elif num == 5:
#             shuru().bank_inquriy()
#         elif num == 6:
#             print("欢迎下次光临！！！")
#             close()
#             break
#         else:
#             print("输入非法！请重新输入！！！")
#     else:
#         print("您输入非法！请重新输入！！！")



