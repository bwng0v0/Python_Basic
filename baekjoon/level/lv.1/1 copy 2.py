dice = list(map(int,input().split()))

maxi = 0
for i in range(len(dice)):
    if dice.count(maxi) < dice.count(dice[i]): #조건문이 잘못됨 브레이크포인트로 봤다면..
        maxi = dice[i]

if dice.count(maxi) == 3:
    print(10000+(1000*maxi))  
elif dice.count(maxi) == 2:
    print(1000+(100*maxi))
else:
    print(max(dice)*100)