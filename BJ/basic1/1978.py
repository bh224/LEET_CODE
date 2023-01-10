#1978
"""
첫 줄에 수의 개수 N이 주어진다
그 다음 주어지는 수들 중 소수의 개수를 출력
"""
N = int(input())
data = list(map(int, input().split()))

def prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
list = []
for i in data:
    if i == 1:
        continue
    result = prime_num(i)
    if not result:
        continue
    else:
        list.append(i)

print(len(list))