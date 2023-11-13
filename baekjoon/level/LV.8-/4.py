N = int(input())
arr = list(map(int,input().split()))

cnt = 0
for i in arr:
    if i == 1:
        continue
    is_prime = 1
    for j in range(2,i):
        if i%j==0:
            is_prime = 0
            break
    if is_prime == 1:
        cnt += 1
    
print(cnt)