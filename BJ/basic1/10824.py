#10824 네 수
"""
네 자연수 A, B, C, D가 주어지면
A와 B, C와 C를 붙인 수의 합을 출력
"""
A, B, C, D = list(input().split())
first = A+B
second = C+D
result = int(first) + int(second)
print(result)
