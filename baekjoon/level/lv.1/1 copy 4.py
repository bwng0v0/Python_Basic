import sys
total = int(input())
N = int(input())
sum = 0
for i in range(N):
    price,num = map(int,sys.stdin.readline().strip().split())
    sum += price*num

if sum == total:
    print("Yes")
else:
    print("No")