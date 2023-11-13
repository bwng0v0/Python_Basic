N = int(input())
"""
while N>1:

    for num in range(2,N+1): #와 이것도 범위오류라고?
        is_p = 1
        for i in range(2,num):
            if num%i==0:
                is_p = 0
                break
        if is_p == 1 and N%num==0:
            N = N//num  
            print(num)
            break
"""
while N>1:
    for i in range(2,N+1):
        if N%i == 0:
            N //= i
            print(i)
            break