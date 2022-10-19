#11650
"""
점 N개가 주어지고 각 점의 좌표를 x좌표가 증가하는 순으로
x좌표가 같으면 y좌표가 증가하는 순으로 출력
"""

N = int(input())

nums = []

for _ in range(N):
    points = list(map(int, input().split()))
    nums.append(points)

# print(nums)
nums.sort()
for i in nums:
    print(i[0],i[1])
