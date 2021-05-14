# 列表转数据库
def Excel_to_db():
    import pymysql
    import xlwt
    import xlrd
    # 创建数据库连接
    con = pymysql.connect(host="localhost",user="root",password="",database="excel")
    couser = con.cursor()
    sql = "insert into 销售数据(ntime,clothes,price,stock,salenum) values(%s,%s,%s,%s,%s)"
    # 打开文件
    rb = xlrd.open_workbook(filename="H:\python项目笔记\day13/任务\\12月份衣服销售数据.xlsx",encoding_override=True)
    # 选取sheet页
    sheet1 =rb.sheet_by_index(0)
    # 获取最大行数据
    rows = sheet1.nrows
    for i in range(1,rows):
        ntime = sheet1.cell_value(i,0)
        clothes = sheet1.cell_value(i,1)
        price = sheet1.cell_value(i,2)
        stock = sheet1.cell_value(i,3)
        salenum = sheet1.cell_value(i,4)
        values = (ntime,clothes,price,stock,salenum)
        couser.execute(sql,values)
        con.commit()
    couser.close()
    con.close()