# 1. 두 수의 합

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1] 
# 합이 target 이 되는 두 수의 인덱스를 출력
import time

nums = [2,7,11,15]
target = 9

#첫번째 방법 : 비교
#단순 이중for문으로 경우의 수를 다 더하기

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print(f'[{i},{j}]')


#두번째 방법 : 조회
#딕셔너리의 key값을 조회하는 방법을 사용하여 조회
#배열의 요소를 key, 인덱스를 value로 하는 딕셔너리를 만들어서
#key값으로 조회하면 바로 인덱스를 찾을 수 있다

dict = {}
for i, num in enumerate(nums):
    if target - num in dict:
        print(f'[{dict[target-num]},{i}]')
    else:
        dict[num] = i




