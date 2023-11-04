def two_sum(nums, target):
    left, right = 0, len(nums) - 1  # 리스트의 시작과 끝 인덱스를 가리키는 포인터 초기화
    
    while left < right:
        current_sum = nums[left] + nums[right]  # 현재 두 원소의 합 계산
        
        if current_sum == target:
            return [nums[left], nums[right]]  # 합이 target과 일치하면 해당 두 원소 반환
        elif current_sum < target:
            left += 1  # 합이 작으면 왼쪽 포인터를 오른쪽으로 이동
        else:
            right -= 1  # 합이 크면 오른쪽 포인터를 왼쪽으로 이동
    
    return []  # 합이 target과 일치하는 원소를 찾지 못한 경우 빈 리스트 반환

nums = list(map(int,input().split()))
target = int(input())
print(two_sum(nums,target))
