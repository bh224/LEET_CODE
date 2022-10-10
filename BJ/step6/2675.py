#2675
"""
테스트케이스의 개수 T
반복횟수 R과 문자열 S가 공백으로 주어지고
S의 순서별로 R번 반복하여 출력
"""

import sys

T = int(input())
for _ in range(T):
    R, S = sys.stdin.readline().split()
    new_S = ""
    for i in S:
        new_S += i * int(R)
    print(new_S)
        

# R, S = sys.stdin.readline().split()
# for i in S:
#         print(i*int(R))

