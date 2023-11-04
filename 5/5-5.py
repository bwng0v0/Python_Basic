def get_Prime_or_Not( n ):
    is_Prime = 1
    for i in range(2,n):
        if n%i==0:
            is_Prime = 0
    if is_Prime == 1:
        print("Prime")
    else:
        print("Not Prime")


n = int(input())
get_Prime_or_Not(n)