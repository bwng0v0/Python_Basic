num,N = map(int,input().split())
arr = []
top = 1
while num>=N**top: # > 을 >=로 수정: ex) 2 2 output: 2
   top += 1

for i in range(top-1,-1,-1):
   arr.append(num//N**i)
   num = num%N**i

for i in range(len(arr)):
   if arr[i] >= 10:
      arr[i] = chr(arr[i]+55)
   
for i in arr:
   print(i,end='')