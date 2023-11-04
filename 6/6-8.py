data_num,find_num = map(int,input().split())
data = {}
find = []
for i in range(data_num):
    tmp_key ,tmp_value = input().split()
    data[tmp_key] = tmp_value

for i in range(find_num):
    tmp_key = input()
    find.append( data[tmp_key] )

for i in range(find_num):
    print(find[i])