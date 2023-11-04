def get_side(n):
    x = int(n[0]) + int(n[1])
    if x < 10:
        x = str(x)
        x = '0'+ x
    return str(x)

def get_new( n , x ):
    new = n[1]+x[1]
    return new

#시작점 ____________________________ 아니 캐스팅(형변환) 자주일어나는거 ㄹㅇ 개어렵네
n = str(input())
if len(n) < 2 :
    n = '0'+n

cycle = 0
original = n

while True:
    x = get_side(n)
    n = get_new(n,x)
    cycle += 1
    if original == n:
        print(cycle)
        break
