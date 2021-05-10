a = []
w = open(file="scores.txt",mode="r+",encoding="utf-8")
# w.write("罗恩 23 35 44\n")
# w.write("哈利 60 77 68 88 90\n")
# w.write("赫敏 97 99 89 91 95 90\n")
# w.write("马尔福 100 85 90")
b = w.readlines()
for i in b :
    c = i.replace("\n","").replace(" ",",").split(",")
    for j in c:
        if j.isdigit():
            a.append(j)
a = [int(x) for x in a]
print(a)
scores = sum(a)
print(scores)


