a = [1,5,21,30,15,9,30,24]
b = []
for n in a:
    if n%5==0:
        b.append(n)
print(b)
sum = sum(b)
print("5的倍数的和为：",sum)

