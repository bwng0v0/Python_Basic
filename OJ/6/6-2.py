arr = list(map(int,input().split()))
avrg = sum(arr)/len(arr)

dist = []
for i in range(len(arr)):
    dist.append(abs(arr[i]-avrg))

min_index = dist.index(min(dist))

print(min_index)