#11021
"""
테이스 케이스 개수 T
각 테스트 케이스마다  "Case #x: "를 출력한 다음, A+B를 출력
"""
import sys

T = int(sys.stdin.readline())
for i in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {A+B}")

