def getGCD(a,b):
        while b > 0:
            a, b = b, a % b
            print(f"{a} {b}")
        return a

a,b = map(int,input().split())
print(getGCD(a,b))