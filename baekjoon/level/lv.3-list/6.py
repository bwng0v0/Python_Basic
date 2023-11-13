N,M = map(int,input().split())
arr = []
for i in range(N):
    arr.append(i+1)

for i in range(M):
    a,b = map(int,input().split())
    tmp = arr[a-1]
    arr[a-1] = arr[b-1]
    arr[b-1] = tmp

print(*arr)