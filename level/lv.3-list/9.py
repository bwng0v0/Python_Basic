N = int(input())
arr = []
arr = list(map(int,input().split()))
fake = []

maxi = max(arr)
for item in arr:
    fake.append(item/maxi*100)

fake_avg = 0
for i in fake:
    fake_avg += i

fake_avg /= len(fake)

print(fake_avg)