arr = []
for i in range(30):
    arr.append(i+1)
for i in range(28):
    num = int(input())
    arr.remove(num)

print(min(arr))
print(max(arr))