test = int(input())
for i in range(test):
    n,s = map(str,input().split()) #각각 다른 자료형으로 받을수는 없나
    n = int(n)
    for c in s:
        for i in range(n):
            print(c,end='')
    print('')