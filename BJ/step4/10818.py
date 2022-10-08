#10818.py
"""
N개의 숫자 중  최솟값과 최댓값을 공백을 두고 출력
"""

#1 
N = int(input())
while True:
    nums = list(map(int, input().split()))
    if len(nums) != N:
        continue
    else: print(min(nums), max(nums))

#2 
# import sys

# N = int(input())
# while True:
#     nums = list(map(int, sys.stdin.readline().split()))
#     if len(nums) != N:
#         continue
#     else: print(min(nums), max(nums))
#     break
