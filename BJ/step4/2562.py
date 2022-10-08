# 2562
"""
9개의 서로 다른 자연수 중 최댓값을 찾고 그 최댓값이 몇 번째 수 인지 출력
"""

import sys

nums = [ int(sys.stdin.readline().strip()) for i in range(9) ]
mx = max(nums)
print(mx, nums.index(mx)+1, sep="\n")

