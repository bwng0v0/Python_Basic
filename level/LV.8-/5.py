start = int(input())
end = int(input())

mini = end
sum = 0

for num in range(start,end+1):
    if num == 1:
        continue

    is_prime = 1
    for i in range(2,num):
        if num%i==0:
            is_prime = 0
            break
    if is_prime == 1:
        sum += num
        if mini > num:
            mini = num

if sum == 0:
    print(-1)
else:
    print(sum)
    print(mini)