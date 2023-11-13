import math

n = int(input())
r = int(input())

print(f"nCr = {math.comb(n,r)}")
print(f"nPr = {math.perm(n,r)}")
print(f"n! = {math.factorial(n)}")
print(f"최대공약수 = {math.gcd(n,r)}")
print(f"최소공배수{math.lcm(n,r)}")

