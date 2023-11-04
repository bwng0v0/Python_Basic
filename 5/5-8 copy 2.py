ABC = {0:'A',1:'B',2:'C'}
arr = [ [],[],[] ]

def auto(number)
    "특정값을 찾아서 있던곳 외에 놓일수 있는곳에 자동으로 놓음"
    global arr
    global n
    for i in arr: # 넘버 찾아서 지우고
        if arr[i].count(number) == 1:
            arr[i].remove(number)
    #있던곳 외에 놓일수있는곳에 자동으로 놓음(규칙이 있어야하는데)
    
    

n = int(input())
if n%2 == 0:
    swich = 2
for i in range(n,0,-1):
    arr[0].append(i)

auto(1)
pass

print(arr)