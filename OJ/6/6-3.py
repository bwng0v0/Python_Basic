arr = list(map(int,input().split()))

up = sorted(arr)
down = sorted(arr , reverse=1)

res = 0 
for i in range(len(arr)):
    res += up[i]*down[i]

print(res)
