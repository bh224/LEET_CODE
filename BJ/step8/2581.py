#2581
"""
자연수 M, N이 주어지고 M 이상 N 이하의 자연수 중 소수인것을 골라
소수의 합과 최솟값을 출력
소수가 없는 경우 -1 출력
"""
pn = []

def PrimeNum(num):
    for k in range(2, num):
        if num % k == 0:
            return False
    return True

M = int(input())
N = int(input())

for i in range(M, N+1):
    if i == 1:
        continue
    elif PrimeNum(i):
        pn.append(i)

if len(pn) > 0:
    print(sum(pn))
    print(min(pn))
else:
    print(-1)
