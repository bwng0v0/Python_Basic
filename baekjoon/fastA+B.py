import sys
N = int(sys.stdin.readline().strip())
list = []
for i in range(N):
    A,B = map(int , sys.stdin.readline().strip().split())
    list.append(A+B)
for i in range(N):
    print(list[i])