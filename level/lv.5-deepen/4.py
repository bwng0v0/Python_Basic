s = input()
is_pel = 1
for i in range(len(s)//2):
    if s[i] == s[-1-i]:
        continue
    else:
        is_pel = 0
        break

print(is_pel)