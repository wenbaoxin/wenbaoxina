import random
# 编写程序模拟证件上传的功能，让用户输入证件的路径，并拷贝到一个统一的图片路径下
a= []
url = input("请输入您的证件的存储路径：")
f1 = open(file=url,mode="rb")

file = random.randint(0,99999999999)

f2 = open(file="D:\python\zuoye3\\" + str(file) + ".jpg",mode="wb")

a = f1.read()
f2.write(a)

f1.close()
f2.close()
print("上传成功")