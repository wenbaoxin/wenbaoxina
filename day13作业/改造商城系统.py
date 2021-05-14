# import xlwt
# wt = xlwt.Workbook()
# sheet =wt.add_sheet("商品信息")
# sheet.write(0,0,"带定义的秋裤")
# sheet.write(0,1,1999)
# sheet.write(1,0,"护膝")
# sheet.write(1,1,789)
# sheet.write(2,0,"卫龙面筋")
# sheet.write(2,1,777)
# sheet.write(3,0,"三只松鼠大礼盒")
# sheet.write(3,1,89)
# sheet.write(4,0,"可口可乐/提")
# sheet.write(4,1,399)
# sheet.write(5,0,"炫龙dd2")
# sheet.write(5,1,5999)
# sheet.write(6,0,"卡西欧")
# sheet.write(6,1,1299)
# sheet.write(7,0,"小熊饼干")
# sheet.write(7,1,489)
# sheet.write(8,0,"现抓的活鬼")
# sheet.write(8,1,3999)
# wt.save("我的商城.xls")
import xlrd
rb = xlrd.open_workbook(filename="H:\PycharmProjects\day13\\我的商城.xls",encoding_override=True)
sheet1 = rb.sheet_by_index(0)
row = sheet1.nrows
col = sheet1.ncols
for i in range(row):
    print(sheet1.row_values(i))