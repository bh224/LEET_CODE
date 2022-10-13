#1979
"""
주어진 수 N개 중에서 소수가 몇 개인지 출력
"""

count = 0

def PrimeNum(N):
    for i in range(2, N):
        if N % i == 0:
            return False
    return True

N = int(input())
a = list(map(int, input().split()))

for j in a:
    if j == 1:
        continue
    if PrimeNum(j):
        count += 1

print(count)

