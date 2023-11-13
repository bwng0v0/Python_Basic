N = int(input())
increas = 6 #최초 증가폭은 6 1->7
count = 1 #최초 지나는 방 수는 1
now_range = 1 #최초 범위는 1 하나
while now_range<N: #N이 범위안에 안들어온다면
    now_range += increas #증가폭만큼 범위 증가
    increas += 6 #증가폭 패턴에 따라 늘려주고
    count += 1 #지나야하는 방수 +1
print(count)#지나야하는 방 수 출력
"""
1
2~7 5
8~19 11
20~37 17
38~61 23
"""