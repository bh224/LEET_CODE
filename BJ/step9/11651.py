#11651
"""
점 N개가 주어지고 y좌표가 증가하는 순으로, y,x좌표가 같으면 x좌표가 증가하는 순으로 출력
"""

N = int(input())

nums = []

for _ in range(N):
    points = tuple(map(int, input().split()))
    nums.append(points)
print(nums)
nums.sort(key=lambda x: (x[1], x[0]))

for i in nums:
    print(i[0],i[1])