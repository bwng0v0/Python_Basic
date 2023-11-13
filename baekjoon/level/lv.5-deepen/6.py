#45 -
#61 =
s = input()
sum = len(s)
for i in range(len(s)-1):
    if s[i] == 'c': # c라면
        if s[i+1] == '-' or s[i+1] == '=':
            sum -=1
            continue
        else:
            continue

    if s[i] == 'd': # d 라면
        if s[i+1] =='-':
            sum -= 1
            continue
        #and는 오른쪽으로 하나씩 검사하네!!!!!!!!!!!
        #인덱스에러 날수도 있는거 앞에다 (남은인덱스>검사할 뒤 인덱스) 하면 에러안남 ㅋㅋ
        elif s[i+1]=='z' and len(s)-(i+1)>1 and s[i+2]=='=': 
            sum -= 2
            continue
        else:
            continue

    if s[i] == 'l': # l이라면
        if s[i+1] == 'j':
            sum -= 1
            continue
        else:
            continue

    if s[i] == 'n': # n이라면
        if s[i+1] == 'j':
            sum -= 1
            continue
        else:
            continue

    if s[i] == 's': # s라면
        if s[i+1] == '=':
            sum -= 1
            continue
        else:
            continue

    if s[i] == 'z':
        if s[i+1] == '=' and s[i-1] != 'd':
            sum -= 1
            continue
        else:
            continue
print(sum)