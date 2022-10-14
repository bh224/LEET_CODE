#1929
"""
M이상 N이하의 소수를 모두 출력
"""
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

