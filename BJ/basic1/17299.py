#17299
"""
크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오등큰수 NGF(i)를 구하려고 한다.
Ai가 수열 A에서 등장한 횟수를 F(Ai)라고 했을 때, Ai의 오등큰수는 오른쪽에 있으면서 
수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 
그러한 수가 없는 경우에 오등큰수는 -1이다
수열의 크기와 원소가 주어지고
오등큰수를 출력
"""

#2 
"""
스택에는 인덱스를 넣어두는 것이 좋고
각 요소의 카운터를 딕셔너리로 만들어 인덱스로 조회하는 것이 빠르다
"""

from collections import Counter
from sys import stdin

n = int(input())
nums = list(map(int, input().split()))
nums_count = Counter(nums)
result = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and nums_count[nums[stack[-1]]] < nums_count[nums[i]]:
      result[stack.pop()] = nums[i]
      print('i', i, 'result', result)
    stack.append(i)

print(*result)

#1 시간초과
from collections import deque
import sys

N=int(input())
A = list(map(int, sys.stdin.readline().split()))
F = list(map(lambda x : A.count(x), A)) 
result = [-1] * 7
for i in range(N):
  # print(i,"i", n, )
  st = deque(F[i+1:])
  n = len(F)-1
  for si in range(n):
    # print(f'{si}째 {st}')
    if len(st) == 0:
      break
    if F[i] < st[0]:
      result[i] = A[i+si+1]
      # print("업뎃", result)
      break
    else:
      st.popleft()

print(*result)
