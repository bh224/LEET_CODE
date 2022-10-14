# 4948
"""
베르트랑 공준
자연수 N에 대해 N ~ 2N 까지 소수의 개수를 출력
"""
import math
import time
from tkinter import E
from turtle import end_fill

# 2 소수  리스트를 먼저 구해놓기

start = time.time()

def PrimeNum(N):
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return False
    return True

all_nums = [_ for _ in range(2, 123456 * 2 + 1)]
prime_nums = list(filter(PrimeNum, all_nums))

while True:
    N = int(input())

    if N == 0:
        break

    count = 0

    for j in prime_nums:
        if N < j <= N *2:
            count += 1
            end = time.time()
    print(count)
    print(f'{end-start:.3f} sec')






# 1 시간초과

start = time.time()

def PrimeNum(N):
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

while True:
    n = int(input())
    if n == 0:
        break
    N = n * 2
    count = 0
    for i in range(n+1, N+1):
        if i == 1:
            continue
        if i == 2:
            continue
        else:
            for j in range(2, int(math.sqrt(i))+1):
                if i % j == 0:
                    break
            else: 
                count += 1
                end = time.time()

    print(count)
    print(f'{end-start:.3f} sec')