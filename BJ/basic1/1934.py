#1934
"""
두 자연수 A, B에 대해 A의 배수이면서 B의 배수인 자연수를 공배수라고 한다
첫째줄에 테스트케이스 개수 T
최소공배수 출력
"""

import sys

#최대공약수
def fun_num(a, b):
    min_list = []
    for i in range(1, b+1):
        if a % i == 0 and b % i == 0:
            min_list.append(i)
    return max(min_list)

T = int(input())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    max_sub = fun_num(A, B)
    #최소공배수
    min_multi = (A*B) // max_sub
    print(min_multi)

