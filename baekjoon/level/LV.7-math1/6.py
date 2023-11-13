N = int(input())
indx = 1
way = 1
#단계찾는 와일
while N>indx:
    N -= indx
    indx += 1
    #방향 전환
    if way==1:
        way=0
    else:
        way=1

if way==1:
    x = indx
    y = 1
    for i in range(N-1):
        x -= 1
        y += 1
else:
    x = 1
    y = indx
    for i in range(N-1):
        x += 1
        y -= 1

print(f"{x}/{y}")