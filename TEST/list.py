# end=연습
# 전역변수는 메인함수 밖에서도 값을 수정할수있는가
# 함수 사용 연습

dic = {0:'A',1:'B',2:'C'}
print(f"{dic.get(2)}")

list = [0,1,2,3,4,5,6,7,8,9]
print(f"{list[1:10:2]}")

list.sort(reverse=True)
print(list)


print(list.count(4))

list.insert(4,4)
print(list)

print(list.count(4))


list.remove(4)
print(list)

list.remove(4)
print(list)
list.sort()
print(list)

