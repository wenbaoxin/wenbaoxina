class jisuanqi():
    def add(self,a,b):
        return a + b
    def jian(self,a,b):
        return a - b
    def cheng(self,a,b):
        return a * b
    def chu(self,a,b):
        return a / b


# a = input("请输入数字a：")
# a = int(a)
# b = input("请输入数字b：")
# b = int(b)
# print("1、相加")
# print("2、相减")
# print("3、相乘")
# print("4、相除")
# print("q、退出")
# while True:
#     valuel = input("请输入您要执行的操作编号:")
#     # if valuel.isdigit():
#     if valuel == "1":
#         print(a,"+",b,"=",add(a,b))
#     elif valuel == "2":
#         print(a,"-",b,"=",jian(a,b))
#     elif valuel == "3":
#         print(a,"x",b,"=",cheng(a,b))
#     elif valuel == "4":
#         print(a,"/","b","=",chu(a,b))
#     elif valuel == "q" or valuel == "Q":
#         break
#     else:
#         print("您的输入非法，请重新输入")