code = list(input())
sum = 0
# 65(A) ~ 90(Z)
for c in code:
    if c <= 'C':
        sum += 3
    elif c <= 'F':
        sum += 4
    elif c <= 'I':
        sum += 5
    elif c <= 'L':
        sum += 6
    elif c <= 'O':
        sum += 7
    elif c <= 'S':
        sum += 8
    elif c <= 'V':
        sum += 9
    elif c <= 'Z':
        sum += 10
    else:
        sum += 11
print(sum)