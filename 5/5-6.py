def get_nCr(n,r):
    return factorial(n) / (factorial( n-r )*factorial(r))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

n,r = map(int , input().split()) # 과정좀 자세히 알아야할듯;;
print(f"{get_nCr(n,r):.0f}")
