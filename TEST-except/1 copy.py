while True:
    try:
        n = int(input())
        if 0<=n and n<=50:
            break
        else:
            print("retry")
    except:
        print("Error")

print(n)