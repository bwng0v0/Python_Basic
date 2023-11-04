arr = []
score = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
for i in range(20):
    arr.append(list(map(str,input().split())))

score_sum = 0
major_sum = 0
for i in range(20):
    if arr[i][2] != 'P':
        score_sum += float(arr[i][1]) #리스트안의 i번째 원소 안의 n번째 원소
        major_sum += float(arr[i][1])*score.get(arr[i][2])

print(major_sum/score_sum)