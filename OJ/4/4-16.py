n = int(input())
is_prime = 1
for i in range(2,n):
    if n%i == 0:
        is_prime = 0

if is_prime == 0:
    print("Not Prime")
else:print("Prime")