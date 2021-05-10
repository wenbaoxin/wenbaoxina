# python复制一张图片到D盘的python文件夹里
f1 = open(file="1.jpg",mode="rb")
f2 = open(file="D:\\python\\j.jpg",mode="wb")

a= f1.read()
f2.write(a)

f2.close()
f1.close()