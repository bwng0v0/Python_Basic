x = int(input())

if x%2==0:
    y = "Even and"
else: y = "Odd and"
if x%3==0:
    print("{} Triple".format(y))
else: print("{} Not Triple".format(y))