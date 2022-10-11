#1712
"""
A는 고정비용 B는 가변비용
손익분기점 BEP를 출력
"""

A, B, C = map(int, input().split())

if B>=C:
    print(-1)
else: print(int((A / (C-B)) + 1))