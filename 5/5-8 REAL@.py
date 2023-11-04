#읽고 로직 분석하기
def hanoi(n, A, B, C):
    if n == 1: 
        res.append([f"{n}: {A} -> {C}"])
        return #끝내는 용인가
        
    hanoi(n-1, A, C, B) # B하고 C를 뒤집네?
    res.append([f"{n}: {A} -> {C}"]) #리스트에 로그를 남기고
    hanoi(n-1, B, A, C) # B A C로 ? 

n = int(input())
res = []
hanoi(n, 'A', 'B', 'C')

for i in res:
    print(*i)
