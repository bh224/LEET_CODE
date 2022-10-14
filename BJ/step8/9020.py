#9020
"""
골드바흐 파티션은 2보다 큰 짝수 N은 두 소수의 합으로 나타낼 수 있다
테스트케이스 개수 T
짝수 n이 주어지면 골드바흐 파티션(소수 두개)를 출력
골드바흐 파티션이 여러개인 경우 두 소수의 차가 제일 작은 것으로 출력
"""
import math 

def PrimeNum(N):
    if N == 1:
        return False
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    n = int(input())
    a = n // 2
    b = n // 2

    for i in range(n//2):
        if PrimeNum(a) and PrimeNum(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1