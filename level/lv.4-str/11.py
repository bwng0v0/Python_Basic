arr = []
while 1:
    try:
        arr.append(input())
    except:
        for i in arr:
            print(i)
        break