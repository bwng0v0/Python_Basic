x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
x = []
x.append(x1)
x.append(x2)
x.append(x3)
y = []
y.append(y1)
y.append(y2)
y.append(y3)
for i in x:
    if x.count(i)==1:
        x4 = i
for i in y:
    if y.count(i)==1:
        y4 = i

print(f"{x4} {y4}")