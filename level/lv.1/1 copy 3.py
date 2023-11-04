hour,min = map(int,input().split())
time = int(input())
while time >= 60:
    time -= 60
    hour += 1

    if hour >= 24:
        hour = 0
    
min += time
if min >= 60:
    min -= 60
    hour += 1

    if hour >= 24:
        hour = 0
print(f"{hour} {min}")