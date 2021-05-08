import pymysql
host = "localhost"
user = "root"
password = ""
database = "bank"
# 针对增，删，改
def update(sql,param):
    # 获取链接
    con = pymysql.connect(host=host,user=user,password=password,database=database)
#     创建控制台
    curser = con.cursor()
    # 执行sql语句
    curser.execute(sql,param)
    # 提交
    con.commit()
    # 关闭
    curser.close()
    con.close()

# 针对查询
def select(sql,param):
    # 获取链接
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    #     创建控制台
    curser = con.cursor()
    # 执行sql语句
    curser.execute(sql, param)
    # 提交
    con.commit()
    # 返回
    return curser.fetchall()
    # 关闭
