def hanoi(n):
    "원반이 홀수일 때"

def stack(where,n):
    "B또는 C에다 n만큼 쌓는"
    if n < 1:
        pass
    
def move(here,there,name1,name2):
    "here에서 there로 이동"
    tmp = here[len(here)-1]
    del here[len(here)-1]
    there.append(tmp)
    print(f"{tmp}: {name1} -> {name2}")


n = int( input() )
A,B,C = [],[],[]
for i in range(n,0,-1):
    A.append(i)
