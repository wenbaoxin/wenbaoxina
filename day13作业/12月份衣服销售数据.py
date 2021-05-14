import xlwt
import xlrd
a = []
b = []
rb = xlrd.open_workbook(filename="H:\python项目笔记\day13/任务\\12月份衣服销售数据.xlsx",encoding_override=True)

sheet = rb.sheet_by_name("12月份各种服饰销售情况")

rows = sheet.nrows
cols = sheet.ncols
for i in range(1,rows):
    c= sheet.cell_value(i,4)
    a.append(c)
avenage = round(sum(a)/len(a),0)
print(avenage)
for j in range(1,rows):
    d = sheet.cell_value(j,4) * sheet.cell_value(j,2)
    b.append(d)
all = sum(b)
all = round(all,1)
print(all)

yrfnum = 0
nzknum = 0
fynum = 0
pcnum = 0
txnum = 0
csnum = 0
while True:
    for i in range(1,rows):
        if sheet.cell_value(i,1) == "羽绒服":
            yrfnum = yrfnum + sheet.cell_value(i,4)
        elif sheet.cell_value(i,1) == "牛仔裤":
            nzknum = nzknum + sheet.cell_value(i,4)
        elif sheet.cell_value(i,1) == "风衣":
            fynum = fynum + sheet.cell_value(i,4)
        elif sheet.cell_value(i,1) == "皮草":
            pcnum = pcnum + sheet.cell_value(i,4)
        elif sheet.cell_value(i,1) == "T血":
            txnum = txnum + sheet.cell_value(i,4)
        elif sheet.cell_value(i,1) == "衬衫":
            csnum = csnum + sheet.cell_value(i,4)
    yrf = round(yrfnum / sum(a),2)
    nzk = round(nzknum / sum(a),2)
    fy = round(fynum / sum(a),2)
    pc = round(pcnum / sum(a),2)
    tx = round(txnum / sum(a),2)
    cs = round(csnum / sum(a),2)
    print(yrf,nzk,fy,pc,tx,cs)
    break
data = []
for i in range(rows):
    k = sheet.row_values(i)
    data.append(k)
print(data)
wb = xlwt.Workbook()
sheet1 = wb.add_sheet("十二月份数据汇总清算")

for z,p in enumerate(data):
    for f,t in enumerate(p):
        sheet1.write(z,f,t)
sheet2 = wb.add_sheet("销售数据")
sheet2.write(0,0,"总销售额为：")
sheet2.write(0,1,all)
sheet2.write(1,0,"平均日销售量：")
sheet2.write(1,1,avenage)
sheet2.write(2,0,"羽绒服每月销售占比：")
sheet2.write(2,1,yrf)
sheet2.write(3,0,"牛仔裤每月销售占比：")
sheet2.write(3,1,nzk)
sheet2.write(4,0,"风衣每月销售占比：")
sheet2.write(4,1,fy)
sheet2.write(5,0,"皮草每月销售占比：")
sheet2.write(5,1,pc)
sheet2.write(6,0,"T血每月销售占比：")
sheet2.write(6,1,tx)
sheet2.write(7,0,"衬衫每月销售占比：")
sheet2.write(7,1,cs)
wb.save("十二月份衣服销售总数据.xls")