# 1929
"""
두 자연수 M이상 N이하의 소수를 모두 출력
#1은 에라토스테네스의 체 알고리즘을 이용해 보았다
M부터 N의 제곱근까지의 각 자연수들의 배수를 제외해 준다
남아있는 수들 중 소수가 아닌 수를 제외하고 출력
"""

# 1

import time
import math

start = time.time()

M = 1
N = 1000
square = int(N**0.5)+1 #5

below = [x for x in range(M, square+1)] 
over = [y for y in range(square+1, N+1)] #[6~16]


# 소수판별함수
def is_prime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

# 배수제외함수
def is_multi(n):
  for i in range(len(over)): #index
    if over[i] == 0:
      continue
    if over[i] % n == 0:
      over[i] = 0

for i in below: 
  is_multi(i)

res = set(below + over)
res = list(res)

for r in res:
  if r == 0 or r ==1:
    continue
  if is_prime(r):
    print(r)


#2
import math

def PrimeNum(N):
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if i == 1:
        continue
    if PrimeNum(i):
        print(i)