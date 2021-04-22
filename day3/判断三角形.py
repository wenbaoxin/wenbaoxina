a = input("请输入三角形的边长a：")
a = int(a)
b = input("请输入三角形的边长b：")
b = int(b)
c = input("请输入三角形的边长c：")
c = int(c)
if a==0 or b==0 or c==0 or a+b<=c or a-b>=c:
    print("这不是一个三角形")
elif a+b>c and a-b<c and a==b and b==c :
    print("这是一个等边三角形")
elif a==b or b==c or a==c:
    print("这是一个等腰三角形")
elif a^2+b^2==c^2 or a^2+c^2==b^2 or b^2+c^2==a^2:
    print("这是一个直角三角形")
else:
    print("这是一个普通三角形")
