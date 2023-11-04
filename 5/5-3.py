def get_time(sec):
    hour = sec//3600
    sec %= 3600
    min = sec//60
    sec %= 60
    return [hour,min,sec]


sec = int(input())
time = get_time(sec)
print(f"{time[0]} {time[1]} {time[2]}")