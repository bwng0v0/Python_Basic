num,n = map(int,input().split())
arr = []
for i in range(1,num+1):
    if num%i==0:
        arr.append(i)

if len(arr) >= n:
    print(arr[n-1])
else:
    print(0)