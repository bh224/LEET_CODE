# 1330
"""
두 정수 A, B가 주어졌을 때 A와 B를 비교해서 출력
"""

A, B = map(int, input().split())

if A > B:
    print(">")
elif A < B:
    print("<")
elif A == B:
    print("==")

