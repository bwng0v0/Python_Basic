card_len = int(input())
card =[]
for i in range(card_len):
    card.append((int(input())))
# card = tuple(map(int,input().split()))
num_len = int(input())
num = tuple(map(int,input().split()))

for i in range(card_len):
    if card[i] in num:
        print("1",end=' ')
    else: print("0",end=' ')