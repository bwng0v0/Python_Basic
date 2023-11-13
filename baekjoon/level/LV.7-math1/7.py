A,B,V = map(int,input().split())
day = A-B #하루에 올라가는 양
one_more = V-(A)# 한번만 더 올라가면 정상가는 높이
cnt = one_more//day# 걸리는 날 = 한번만더 올라가면 정상가는 높이//하루에 올라가는 양
if one_more%day > 0:#@@@@@ 조건문을 내가 day != 1 이딴걸로 했었음
    cnt += 1
if A == B:
    cnt = 0
print(cnt+1)