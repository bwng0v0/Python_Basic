size,n = map(int,input().split())
arr = [i+1 for i in range(size)]
try:
    print(int("hello"))
    print(arr[n])
except:
    print("IndexError: list index out of range")