def find_min(arr,index,size):
    # 시작 인덱스가 0보다 작다면 0으로 초기화
    start = index - (size-1)//2 # /는 무조건 float반환하는구나
    if start < 0:
        start = 0
    # 종료 인덱스가 len보다 길다면 len으로 초기화
    end = index + (size//2)+1 # 범위 설정 실수 !종료 인덱스는 범위에 포함되지않음
    if end > len(arr):
        end = len(arr) #실제 인덱스 +1이어도 종료인덱스는 포함X
    # 최소값 탐색후 반환
    mini = arr[start]
    for i in range( start, end ):
        if arr[i] < mini:
            mini = arr[i]
    return mini


window_size = int(input())
arr = list(map(int,input().split()))

for i in range(len(arr)):
    #인덱스 0부터 마지막 인덱스 까지
    print(find_min(arr,i,window_size),end=' ')

"""
5
5 4 3 2 1 1 2 3 4 5

3 2 1 1 1 1 1 1 2 3

현재 WA
5 5 5 4 3 2 1 1 2 3
"""