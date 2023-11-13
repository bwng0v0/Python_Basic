n = int(input())
a,b=1,1
for i in range(1,n):
    if i%2==0:
        a += b
    else:b += a
if n%2==0:
    print(b)
else:print(a)