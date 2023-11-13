s = input()
arr = list()
for i in range(97,122+1):
    arr.append(-1)

for i in s:
    arr[ord(i)-97] = s.index(i)

print(*arr)
# 97 ~ 122