#11022
"""
테이스 케이스 개수 T
각 테스트 케이스마다  "Case #x: A + B = C" 형식으로 출력
"""
import sys

T = int(sys.stdin.readline())
for i in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {A} + {B} = {A+B}")
