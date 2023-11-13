""""
str = input() # 문자열로받고
num = str.split() # 문자열을 리스트로 분리하고
a = int(num[0]) # 각 변수에 직접 리스트의 원소를 형변환해서 넣음
b = int(num[1])
c = int(num[2])
"""
# 1.input으로 문자열을 받고 ex."30 40 50"
# 2. .split메소드로 문자열을 공백 기준으로 나누고 "30","40","50"
# 3. map( 함수, iterable )로 이터러블 객체의 각 요소에 함수를 적용한값을 새로운 이터러블객체로 반환한다.
a,b,c = map(int, input().split())

if a+b>c and a+c>b and b+c>a:
    print("Triangle O")
else: print("Triangle X")