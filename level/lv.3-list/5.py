arr = []
N,M = map(int,input().split())
for i in range(N):
    arr.append(0)
for i in range(M):
    start,end,num = map(int,input().split())
    for j in range(start,end+1):
        arr[j-1] = num

for i in arr:
    print(i,end=' ')