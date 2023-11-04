N = int(input())
for i in range(N):
    change = int(input())
    arr = []
    arr.append(change//25)
    change = change%25
    arr.append(change//10)
    change = change%10
    arr.append(change//5)
    change = change%5
    arr.append(change)
    print(*arr)