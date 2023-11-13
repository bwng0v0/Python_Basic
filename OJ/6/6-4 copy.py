def two_sum(original, target, target_index):
    # 현재 구상중인 디버그는
    # 리스트를 받고 복사, 복사리스트에서 타겟을 인덱스 구분해서 제거
    # 그 후 모든 과정을 복사리스트에서 시작
    #우려되는점은 시간초과, 리스트복사로 인한 메모리오버플로우
    nums = original.copy()
    nums.pop(target_index)

    left, right = 0, len(nums) - 1  # 리스트의 시작과 끝 인덱스를 가리키는 포인터 초기화
    
    while left < right:
        current_sum = nums[left] + nums[right]  # 현재 두 원소의 합 계산
        
        if current_sum == target:
            return 1  # 합이 target과 일치하면
        elif current_sum < target:
            left += 1  # 합이 작으면 왼쪽 포인터를 오른쪽으로 이동
        else:
            right -= 1  # 합이 크면 오른쪽 포인터를 왼쪽으로 이동
    
    return 0  # 합이 target과 일치하는 원소를 찾지 못한 경우

A = int(input())
nums = list(map(int,input().split()))
total = 0

nums.sort() # 투포인터 사용을 위해 정렬

for i in range(len(nums)):
    total += two_sum(nums,nums[i],i)

if A <= 2:
    total = 0

print(total)

"""
2
0 0
out : 0 현재 2
이유: 자신제외 기능의 부재

3
0 3 3
out : 2 AC

2
0 1
out : 0 현재 1
이유: 좋은수를 판별하려면
요소는 3개 이상이어야함 자신외에 다른 두 수가 조건임

3
0 0 0
out : 3 AC

4
0 1 2 3
out : 1 현재 3
123이 좋은수로 나오는데
모두 0+자기자신
1+2=3 만 좋은수여야함

3
0 -5 5
out : 1 현재 3
정렬하면
-5 0 5
이것도 결국 자신 제외

"""