arr = []
lens = []
for i in range(5):
    arr.append(list(input()))
    lens.append(len(arr[i]))

for i in range(max(lens)):
    for j in range(5):
        try:
            print(arr[j][i],end='')
        except:
            continue