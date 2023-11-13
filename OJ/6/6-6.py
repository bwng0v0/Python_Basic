list = list(map(float,input().split()))
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
mini = 0
for i in range(len(list)):
    if list[mini] > list[i]:
        mini = i

print(week[mini])