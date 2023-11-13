while 1:
    N = int(input())
    if N==-1:
        break

    arr = []
    for i in range(1,N):
        if N%i==0:
            arr.append(i)
    
    if N==sum(arr):
        print(f"{N} = ",end='')
        for i in range(len(arr)-1):
            print(f"{arr[i]} + ",end='')
        print(arr[-1])
    else:
        print(f"{N} is NOT perfect.")