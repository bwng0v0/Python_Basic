from decimal import Decimal
# 수정 1: 팩토리얼 재귀함수로 인한 스택오버플로우
# 재귀함수 -> for문 사용
# 수정 2: total 오버플로우
# 초기값을 int(1) -> float(1.0)
# int < float
# 수정 3: 테스트 케이스에서 또 오버플로우가 나는줄알고 decimal모듈로 모두 decimal 자료형으로 연산함
# 수정 4: for문이 n까지 돌아야하는데 range는 매개변수-1까지 돌아감
def exponent(x,n):
    return Decimal(x**n/facto(n))
def facto(n):
    total = Decimal(1.0) 
    for i in range(1,n+1):
        total *= Decimal(i)
    return Decimal(total)

e = Decimal(2.71828)
res = Decimal(0.0)
x,n = map(Decimal , input().split())
for i in range(int(n+1)): # 아?
    res += exponent(x,i)

print(f"{res:.2f}")
