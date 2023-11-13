def get_fbnc(x):
    if x>2:
        return get_fbnc(x-2)+get_fbnc(x-1) 
    elif x==1 or x==2:
        return 1
    elif x<0:
        return 0
    
n = int(input())

x = get_fbnc(n)
print(x)