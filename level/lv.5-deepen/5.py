s = input()
s = s.upper()
arr = []
for i in range(26): #횟수는 25번 맞아 인덱스는 0~24 25개
    arr.append(0)

#대문자 65A ~ 90Z
#소문자 97a ~ 122z
# 65, 97 ,+25
for c in s:
    arr[ord(c)-65] += 1

maxi = max(arr)
if arr.count(maxi) > 1:
    print('?')
else:
    print(chr(arr.index(maxi)+65))