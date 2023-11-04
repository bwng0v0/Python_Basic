N,number = input().split()
arr = []
for c in N:
    if c.isnumeric():
        arr.append(int(c))#인트로 어펜드 해야한다고
        continue
    elif c.isalpha():
        arr.append(ord(c)-55)#아스키 코드 기억한거 칭찬해

res = 0
power = 0
for i in range(1,len(arr)+1):
    res += arr[-i]*(int(number)**power) #와 진법수^지수 순서 바뀌어가지고 0제곱이 1이 안나왔네
    power += 1 #  |-- 여기도 곱하기 제곱이 아니라 곱하기였고 이사람아 ㅋㅋㅋ 서로 바뀌면 어떡하냐

print(res)