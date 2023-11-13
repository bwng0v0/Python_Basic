string = input()
dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
for i in string:
    if i.isalpha() and i.islower():
        dict[i] += 1# dict[key] += 1 은 밸류에다가 하는 연산임
    else: continue

for values in dict.values():
    print(values,end=' ')