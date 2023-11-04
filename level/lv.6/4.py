def color(arr,x,y):
    x -= 1 #인덱스로 변환
    y -= 1
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j] = 1

arr = []
tmp = []
for i in range(100):
    tmp.append(0)
for i in range(100):
    arr.append(tmp.copy()) #아니 참조를 했었다고?

N = int(input())
for i in range(N):
    x,y = map(int,input().split())
    color(arr,x,y)

area = 0
for i in range(100):
    area += sum(arr[i])

print(area)