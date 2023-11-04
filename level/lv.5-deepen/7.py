def is_group(s):
    s = str(s)
    finish = []
    now = s[0]
    for c in s:
        if c != now: #이번에 잡을거랑 들고있던게 다르면
            #쓰레기통에 들고있던걸 넣고
            finish.append(now)
        now = c #그걸 잡아
        #만약 잡은게 쓰레기통에 있던거면 0반환
        if c in finish:
            return 0
    #문제없이 다돌았다면 1반환
    return 1


N = int(input())
arr = []
for i in range(N):
    arr.append(input())

sum = 0
for s in arr:
    sum += is_group(s)
print(sum)