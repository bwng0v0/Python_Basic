def part_reverse(arr,start,end):
    "start부터 end까지"
    #arr = list(arr)
    length = end - start
    if length == 1:
        pass
    else:
        length = (length+1)//2
    for i in range(length):
        tmp = arr[start-1]
        arr[start-1] = arr[end-1]
        arr[end-1] = tmp
        start += 1
        end -= 1

N,M = map(int,input().split())
arr = list()
for i in range(N):
    arr.append(i+1)

for i in range(M):
    start,end = map(int,input().split())
    part_reverse(arr,start,end)
print(*arr)