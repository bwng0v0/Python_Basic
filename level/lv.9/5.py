N = int(input())
x_arr = []
y_arr = []
for i in range(N):
    x,y = map(int,input().split())
    x_arr.append(x)
    y_arr.append(y)
    
max_x = max(x_arr)
max_y = max(y_arr)
min_x = min(x_arr)
min_y = min(y_arr)

area = (max_x-min_x)*(max_y-min_y)
print(area)