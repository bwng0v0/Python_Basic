arr = []
arr = map( int , input().split() )
arr = list(arr)
smallest = arr[4]

for i in range(4):
    if smallest > arr[i]:
        smallest = arr[i]
number = smallest

while True:
    count = 0
    for j in range(5):
        if number%arr[j] == 0:
            count += 1

    if count >= 3:
        print(number)
        break
    
    number += 1
