#2751
"""
N개의 수가 주어졌을 때 오름차순으로 정렬  
"""
import sys

n = int(input())
nums = []
for I in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()

for _ in nums:
    print(_)