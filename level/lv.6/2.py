arr = []
for i in range(9):
    arr.append(list(map(int,input().split())))

maxi = arr[0][0]
max_index = [1,1]
for i in range(9):
    if maxi < max(arr[i]):
        maxi = max(arr[i])
        max_index[0] = i+1
        max_index[1] = arr[i].index(maxi)+1

print(maxi)
print(*max_index)