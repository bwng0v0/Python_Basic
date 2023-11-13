ori = [1,1,2,2,2,8]
find = list(map(int,input().split()))
for i in range(len(ori)):
    ori[i] = ori[i] - find[i]
print(*ori)