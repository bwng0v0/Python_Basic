str = input()
list = []
for c in str:
    if c.isalpha():
        pass
    else: 
        list.append(c)
for i in list:
    str = str.replace(i,'')
print(str)