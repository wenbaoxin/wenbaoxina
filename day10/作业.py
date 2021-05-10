# 使用数据库工具将文件中的数据写入到数据库中。并统计所有人的资产总和！
import pymysql
con = pymysql.connect(host="localhost",user="root",password="",database="资产")
curser = con.cursor()
user =[]
avenge = 0

a = open(file="用户数据.txt",mode="r+")
b = a.readlines()
for i in b:
    c = i.replace("\n","").split(",")
    user.append(c)
for j in user:
    sql = "insert into 个人资产 values(%s,%s,%s)"
    param = [j[0],j[1],j[2]]
    curser.execute(sql,param)
    con.commit()
    avenge = avenge+int(j[2])
print("资产总和为：",avenge)


