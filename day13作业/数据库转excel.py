def Db_to_excel():
    import pymysql
    import xlwt
    con = pymysql.connect(host="localhost",user="root",password="",database="资产")
    curser = con.cursor()
    sql = "select * from 个人资产"
    curser.execute(sql,[])
    a = curser.fetchall()
    wb = xlwt.Workbook()
    sheet = wb.add_sheet("资产明细")
    for i ,j in enumerate(a):
        for x,y in enumerate(j):
            sheet.write(i,x,y)
    wb.save("资产.xls")
    curser.close()
    con.close()