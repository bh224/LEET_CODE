#2108
"""
N은 홀수라고 가정
산술평균: N개의 수들의 합을 N으로 나눈 값
중앙값: N개의 수들을 증가하는 순서로 나열했을 때 중아에 위치하는 값
최빈값: N개의 수들 중 가장 많이 나타나는 값
범위: N개의 수들 중 최댓값과 최솟값의 차이

첫째줄에 수의 개수 N이 주어진다(홀수)
그 다음 한 줄에 하나씩 N개의 정수가 주어진다

산술평균(소수점이하 첫째자리 반올림)
중앙값
최빈값 (여러개 있을 경우 두번째로 작은 값)
범위 를 출력
"""
import sys

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

#오름차순정렬
nums.sort() 

#산술평균
avg = sum(nums) / N
print(round(avg))

#중앙값
idx = int((len(nums)-1)/2)
print(nums[idx])

#최빈값 -> 시간초과
# counts = []
# for i in nums:
#     cnt = nums.count(i)
#     counts.append(cnt)
# if counts.count(max(counts)) >1:
#     idx = counts.index(1, 1)
#     print(nums[idx])
# else:
#     idx = counts.index(max(counts))
#     print(nums[idx])
counts = []
d = {}
for k in nums:
  d[k] = d.setdefault(k,0) +1

mx = max(d.values())

for i in d:
  if d[i] == mx:
    counts.append(i) 

if len(counts) > 1:
  print(counts[1])
else:
  print(counts[0])

#범위
mx = max(nums)
mn = min(nums)
print(mx-mn)