s = list(input())
print(f"{s[0]}({ord(s[0])}) , {s[1]}({ord(s[1])})")
if s[0] > s[1]:
    print('앞이 더 큼')
else:
    print('뒤가 더 큼')