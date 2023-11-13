num1,num2 = input().split()

#리스트로 변환
num1 = list(num1)
num2 = list(num2)
# 그리고 반전
num1.reverse()
num2.reverse()

# join너무좋은데?
# 이터러블 -> 문자열 개꿀따라시
num1 = ''.join(num1)
num2 = ''.join(num2)

if int(num1) > int(num2):
    print(num1)
else:
    print(num2)