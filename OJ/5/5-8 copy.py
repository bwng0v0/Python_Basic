ABC = {0:'A',1:'B',2:'C'}
arr = [[],[],[]]
swich = 1

def stack(n,here,there):
    if n>1:
        global swich
        swich += 1
        stack(n-1,here,(swich%2+1))
        move(here,there)
        stack(n-1,(swich%2),there)
    elif n == 1:
        move(here,there)

def move(here,there):
    tmp = arr[here].pop()
    arr[there].append(tmp)
    print(f"{tmp}: {ABC.get(here)} -> {ABC.get(there)}")

n = int(input())
if n%2 == 0:
    swich = 2
for i in range(n,0,-1):
    arr[0].append(i)

pass

#홀수 기준
move(0,2)#1놓고

move(0,1)#2놓고
move(2,1)

move(0,2)#3놓고
move(1,0)
move(1,2)
move(0,2)

move(0,1)#4놓고 B에다 3~1을 쌓아
move(2,)
move()

print(arr)